-- insert-data.sql
-- insert sample data: 5 speakers, 10 attendees, 7 sessions, 15 registrations

-- 5 speakers
INSERT INTO speakers (first_name, last_name, email, topic) VALUES
('Alice', 'Johnson', 'alice.johnson@gmail.com', 'AI & Ethics'),
('Bob', 'Smith', 'bob.smith@outlook.com', 'Cloud Architecture'),
('Carla', 'Mendez', 'carla.mendez@gmail.com', 'Data Visualization'),
('Daniel', 'Lee', 'daniel.lee@gmail.com', 'Cybersecurity'),
('Eve', 'Nguyen', 'eve.nguyen@bing.com', 'DevOps');

-- 10 attendees
INSERT INTO attendees (first_name, last_name, email, organization) VALUES
('Frank', 'Morris', 'frank.morris@gmail.com', 'OpenTech'),
('Grace', 'Huang', 'grace.huang@gmail.com', 'DataCorp'),
('Hector', 'Diaz', 'hector.diaz@outlook.com', 'Cloudy Inc'),
('Ivy', 'Kim', 'ivy.kim@bing.com', 'StartUpX'),
('Jake', 'Olsen', 'jake.olsen@gmail.com', 'ConsultCo'),
('Kari', 'Patel', 'kari.patel@outlook.com', 'FinServ'),
('Liam', 'Ng', 'liam.ng@gmail.com', NULL),
('Maya', 'Singh', 'maya.singh@outlook.com', 'HealthTech'),
('Noah', 'Adams', 'noah.adams@gmail.com', 'Retailer'),
('Olivia', 'Brown', 'olivia.brown@bing.com', 'EduLabs');

-- 7 sessions
INSERT INTO sessions (title, speaker_id, session_date, session_time) VALUES
('Intro to AI Ethics', 1, '2025-11-02', '09:00'),
('Scaling Cloud Systems', 2, '2025-11-02', '11:00'),
('Data Viz for Storytelling', 3, '2025-11-03', '10:00'),
('Practical Cybersecurity', 4, '2025-11-03', '14:00'),
('DevOps Pipelines', 5, '2025-11-04', '09:30'),
('Advanced Machine Learning', 1, '2025-11-04', '11:30'),
('Cloud Cost Optimization', 2, '2025-11-04', '15:00');

-- 15 registrations
INSERT INTO registrations (attendee_id, session_id) VALUES
(1, 1),
(1, 2),
(2, 1),
(2, 3),
(3, 2),
(3, 7),
(4, 3),
(4, 4),
(5, 1),
(5, 5),
(6, 6),
(7, 5),
(8, 6),
(9, 2),
(10, 4);
