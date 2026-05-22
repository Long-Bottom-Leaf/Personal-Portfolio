-- queries.sql

-- 1) Find all sessions a specific attendee is registered for (given email)

    SELECT
        sessions.session_id,
        sessions.title,
        sessions.session_date,
        sessions.session_time,
        speakers.first_name || ' ' || speakers.last_name AS speaker_name
    FROM sessions
    JOIN registrations ON sessions.session_id = registrations.session_id
    JOIN attendees ON registrations.attendee_id = attendees.attendee_id
    LEFT JOIN speakers ON sessions.speaker_id = speakers.speaker_id
    WHERE attendees.email = $1
    ORDER BY sessions.session_date, sessions.session_time;

-- 2) Given a session title, list all attendees registered for that session

    SELECT
        attendees.attendee_id,
        attendees.first_name,
        attendees.last_name,
        attendees.email,
        attendees.organization
    FROM attendees
    JOIN registrations ON attendees.attendee_id = registrations.attendee_id
    JOIN sessions ON registrations.session_id = sessions.session_id
    WHERE sessions.title ILIKE $1
    ORDER BY attendees.last_name, attendees.first_name;

-- 3) Retrieve the schedule (title, time, and speaker) for all sessions presented by a specific speaker

    SELECT 
        sessions.session_id,
        sessions.title,
        sessions.session_date,
        sessions.session_time,
        speakers.first_name || ' ' || speakers.last_name AS speaker_name
    FROM sessions
    JOIN speakers ON sessions.speaker_id = speakers.speaker_id
    WHERE speakers.email = $1
    ORDER BY sessions.session_date, sessions.session_time;

-- 4) Find all attendees attending at least one session from a specific speaker

    SELECT DISTINCT             -- DISTINCT tells SQL to only return unique rows, avoiding duplicate rows since attendees can register for numerous sessions
        attendees.attendee_id,
        attendees.first_name, 
        attendees.last_name,
        attendees.email,
        attendees.organization
    FROM attendees
    JOIN registrations ON attendees.attendee_id = registrations.attendee_id
    JOIN sessions ON registrations.session_id = sessions.session_id
    JOIN speakers ON sessions.speaker_id = speakers.speaker_id
    WHERE speakers.email = $1
    ORDER BY attendees.last_name, attendees.first_name;

-- 5) List all sessions occurring on a specific date

    SELECT
        sessions.session_id,
        sessions.title,
        sessions.session_date,
        sessions.session_time,
        speakers.first_name || ' ' || speakers.last_name AS speaker_name
    FROM sessions
    LEFT JOIN speakers ON sessions.speaker_id = speakers.speaker_id
    WHERE sessions.session_date = $1
    ORDER BY sessions.session_time;