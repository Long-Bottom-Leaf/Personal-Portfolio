const { Pool } = require('pg');
const fs = require('fs');
const path = require('path');

// PostgreSQL connection
const pool = new Pool({
  user: 'postgres', // This _should_ be your username, as it's the default one Postgres uses
  host: 'localhost',
  database: 'keyin_test', // Change this to reflect your actual database
  password: 'dota2X420p', // Change this to reflect the password you used when setting up Postgres
  port: 5432,
});

/**
 * Creates the database tables, if they do not already exist.
 */
async function createTables() {
  try {
    const sqlPath = path.join(__dirname, '..', 'sql-queries', 'create-tables.sql');
    const createSQL = fs.readFileSync(sqlPath, 'utf8');
    await pool.query(createSQL);

    console.log('Tables created (or already exists).');

  } catch (error) {
    console.error('Error creating tables: ', error.message)
  }
};

/**
 * Inserts a new session into the Sessions table.
 * 
 * @param {string} title - Title of the session
 * @param {number} speakerId - ID of the speaker presenting the session
 * @param {string} date - Date of the session (YYYY-MM-DD format)
 * @param {string} time - Time of the session (HH:MM format)
 */
async function insertSession(title, speakerId, date, time) {
  try {
    const response = await pool.query(
      `INSERT INTO sessions (title, speaker_id, session_date, session_time)
       VALUES ($1, $2, $3, $4) RETURNING session_id`,
      [title, speakerId || null, date, time]
    );

    console.log(`Session inserted with id ${response.rows[0].session_id}`);

  } catch (error) {
    console.error('Error inserting session:', error.message);
  }
};

/**
 * Prints all sessions in the database to the console.
 */
async function displaySessions() {
  try {
    const response = await pool.query(`
      SELECT sessions.session_id,
        sessions.title,
        sessions.session_date,
        to_char(sessions.session_time, 'HH24:MI') AS session_time,
        COALESCE(speakers.first_name || ' ' || speakers.last_name, 'TBD') AS speaker
      FROM sessions
      LEFT JOIN speakers ON sessions.speaker_id = speakers.speaker_id
      ORDER BY sessions.session_date, sessions.session_time;
    `);

    if (response.rowCount === 0) {
      console.log('No sessions found.');
      return;
    }

    console.table(response.rows);

  } catch (error) {
    console.error('Error displaying sessions:', error.message);
  }
};

/**
 * Updates an attendee's email address.
 * 
 * @param {number} attendeeId - ID of the attendee
 * @param {string} newEmail - New email address of the attendee
 */
async function updateAttendeeEmail(attendeeId, newEmail) {
  try {
    const response = await pool.query(
      `UPDATE attendees SET email = $1 WHERE attendee_id = $2 RETURNING *`,
      [newEmail, attendeeId]
    );

    if (response.rowCount === 0) {
      console.log('No attendee found with that ID.');

    } else {
      console.log('Attendee update: ', response.rows[0]);

    }
  } catch (error) {
    if (error.code === '23505') {           // error code 23505 indicates that an INSERT or UPDATE attempted to create a duplicate entry
      console.error('That email is already in use by another attendee.');

    } else {
      console.error('Error updating attendee email: ', error.message);
    }
  }
};

/**
 * Removes an attendee from the database along with their registrations.
 * 
 * @param {number} attendeeId - ID of the attendee to remove
 */
async function removeAttendee(attendeeId) {
  try {
    await pool.query('DELETE FROM registrations WHERE attendee_id = $1', [attendeeId]);
    const result = await pool.query('DELETE FROM attendees WHERE attendee_id = $1 RETURNING *', [attendeeId]);

    if (result.rowCount === 0) {
      console.log('No attendee found with that ID.');

    } else {
      console.log(`Removed Attendee: ${result.rows[0].first_name} ${result.rows[0].last_name}`);

    }
  } catch (error) {
    console.error('Error removing attendee: ', error.message);
  }
};

/**
 * Prints a help message to the console.
 */
function printHelp() {
  console.log('Usage:');
  console.log('  insert <title> <speaker_id> <date> <time> - Insert a session');
  console.log('  show - Show all sessions');
  console.log('  update <attendee_id> <new_email> - Update an attendee\'s email');
  console.log('  remove <attendee_id> - Remove an attendee from the database');
}

/**
 * Runs the CLI app to manage the conference event system.
 */
async function runCLI() {
  await createTables();

  const args = process.argv.slice(2);
  switch (args[0]) {
    case 'insert':
      if (args.length !== 5) {
        printHelp();
        return;
      }
      await insertSession(args[1], parseInt(args[2]), args[3], args[4]);
      break;
    case 'show':
      await displaySessions();
      break;
    case 'update':
      if (args.length !== 3) {
        printHelp();
        return;
      }
      await updateAttendeeEmail(parseInt(args[1]), args[2]);
      break;
    case 'remove':
      if (args.length !== 2) {
        printHelp();
        return;
      }
      await removeAttendee(parseInt(args[1]));
      break;
    default:
      printHelp();
      break;
  }
};

runCLI();

process.on('exit', () => pool.end());     // simply ensures the database connection closes after program exits