CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    password_hash TEXT NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    phone_number VARCHAR(20),
    address TEXT,
    role VARCHAR(20) NOT NULL CHECK (role IN ('ADMIN', 'TRAINER', 'MEMBER')),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE admins (
    admin_id SERIAL PRIMARY KEY,
    user_id INT UNIQUE NOT NULL,
    access_level INT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE
);

CREATE TABLE trainers (
    trainer_id SERIAL PRIMARY KEY,
    user_id INT UNIQUE NOT NULL,
    specialty VARCHAR(100),
    experience_years INT,
    membership_status VARCHAR(20) NOT NULL CHECK (membership_status IN ('ACTIVE', 'INACTIVE', 'SUSPENDED')),
    membership_start_date DATE NOT NULL,
    membership_end_date DATE,
    membership_total_revenue DECIMAL(10, 2) DEFAULT 0.00,
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE
);

CREATE TABLE members (
    member_id SERIAL PRIMARY KEY,
    user_id INT UNIQUE NOT NULL,
    membership_status VARCHAR(20) NOT NULL CHECK (membership_status IN ('ACTIVE', 'INACTIVE', 'SUSPENDED')),
    membership_start_date DATE NOT NULL,
    membership_end_date DATE,
    membership_total_revenue DECIMAL(10, 2) DEFAULT 0.00,
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE
);

CREATE TABLE classes (
    class_id SERIAL PRIMARY KEY,
    class_name VARCHAR(100) NOT NULL,
    description TEXT,
    schedule TIMESTAMP NOT NULL,
    trainer_id INT NOT NULL,
    FOREIGN KEY (trainer_id) REFERENCES trainers(trainer_id) ON DELETE SET NULL
);

CREATE TABLE enrollments (
    enrollment_id SERIAL PRIMARY KEY,
    member_id INT NOT NULL,
    class_id INT NOT NULL,
    enrollment_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (member_id) REFERENCES members(member_id) ON DELETE CASCADE,
    FOREIGN KEY (class_id) REFERENCES classes(class_id) ON DELETE CASCADE,
    UNIQUE (member_id, class_id)
);

CREATE TABLE merchandise (
    merchandise_id SERIAL PRIMARY KEY,
    item_name VARCHAR(100) NOT NULL,
    description TEXT,
    price DECIMAL(10, 2) NOT NULL,
    quantity INT NOT NULL
);  
