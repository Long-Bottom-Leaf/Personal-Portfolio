-- create-tables.sql
-- create tables for speakers, attendees, sessions, and registrations

-- speakers table
CREATE TABLE IF NOT EXISTS speakers (
    speaker_id SERIAL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(150) UNIQUE NOT NULL,
    topic VARCHAR(150) NOT NULL
);

-- attendees
CREATE TABLE IF NOT EXISTS attendees (
    attendee_id SERIAL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(150) UNIQUE NOT NULL,
    organization VARCHAR(150)
);

-- sessions
CREATE TABLE IF NOT EXISTS sessions (
    session_id SERIAL PRIMARY KEY,
    title VARCHAR(150) NOT NULL,
    speaker_id INT REFERENCES speakers(speaker_id) ON DELETE SET NULL,
    session_date DATE NOT NULL,
    session_time TIME NOT NULL
);

-- registrations (junction table)
CREATE TABLE IF NOT EXISTS registrations (
    registration_id SERIAL PRIMARY KEY,
    attendee_id INT NOT NULL REFERENCES attendees(attendee_id) ON DELETE CASCADE,
    session_id INT NOT NULL REFERENCES sessions(session_id) ON DELETE CASCADE,
    UNIQUE (attendee_id, session_id)            -- prevent duplicate registrations
);
