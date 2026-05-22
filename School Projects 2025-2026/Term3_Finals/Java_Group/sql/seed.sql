-- insert users
INSERT INTO users (
    username,
    password_hash,
    email,
    first_name,
    last_name,
    phone_number,
    address,
    role
) VALUES (
    'admin1',
    '$2a$12$ANbyyBtQig9eMVbHq/vM4OqD1UghR2tCrLs0B.CEkMDDuShI9Yy1q',
    'admin@gym.com',
    'John',
    'Doe',
    '709-782-3331',
    '4 Elizabeth Dr, Paradise, NL',
    'ADMIN'
);
INSERT INTO users (
    username,
    password_hash,
    email,
    first_name,
    last_name,
    phone_number,
    address,
    role
) VALUES (
    'trainer1',
    '$2a$10$b/XP.cb4DutiVPCjY2.goedSg0.WvzXUHE2wbmvElrHzrWNqsm1OS',
    'trainer1@gym.com',
    'Alice',
    'Smith',
    '709-364-9233',
    '632 Topsail Rd, St. John''s, NL',
    'TRAINER'
);
INSERT INTO users (
    username,
    password_hash,
    email,
    first_name,
    last_name,
    phone_number,
    address,
    role
) VALUES (
    'maryb123',
    '$2a$10$gG1a5Da/5HkaDqLCZmEnS.VfC9JPs9nXoIGPbT8V1NU/DZjWdBES6',
    'marybrown@gmail.com',
    'Mary',
    'Brown',
    '709-738-4242',
    '250 Blackmarsh Rd, St. John''s, NL',
    'MEMBER'
);

-- insert memberships
INSERT INTO trainers (
    user_id,
    specialty,
    experience_years,
    membership_status,
    membership_start_date,
    membership_end_date,
    membership_total_revenue
) VALUES (
    2,
    'Barre, Yoga, Spin',
    5,
    'ACTIVE',
    '2023-01-01',
    '2024-01-01',
    1200.00
);
INSERT INTO members (
    user_id,
    membership_status,
    membership_start_date,
    membership_end_date,
    membership_total_revenue
) VALUES (
    3,
    'ACTIVE',
    '2023-06-01',
    '2023-07-01',
    600.00
);
-- insert admin
INSERT INTO admins (
    user_id,
    access_level
) VALUES (
    1,
    10
);

-- insert workout classes
INSERT INTO classes (
    class_name,
    description,
    schedule,
    trainer_id
) VALUES (
    'Intro to Barre',
    'A barre class suitable for all levels.',
    '2023-09-01 10:00:00',
    1
);

INSERT INTO classes (
    class_name,
    description,
    schedule,
    trainer_id
) VALUES (
    'HIIT Workout',
    'High-Intensity Interval Training to boost your cardio and strength.',
    '2023-09-02 12:00:00',
    1
);
INSERT INTO classes (
    class_name,
    description,
    schedule,
    trainer_id
) VALUES (
    'Strength Training',
    'Build muscle and improve strength with this intensive class.',
    '2023-09-03 14:00:00',
    1
);

-- insert gym merch
INSERT INTO merchandise (
    item_name,
    description,
    price,
    quantity
) VALUES (
    'Protein Shake',
    'A delicious and nutritious protein shake to fuel your workouts.',
    4.99,
    100
);
INSERT INTO merchandise (
    item_name,
    description,
    price,      
    quantity
) VALUES (
    'Water Bottle',
    'A durable water bottle to keep you hydrated during your exercise.',
    9.99,
    150
);
