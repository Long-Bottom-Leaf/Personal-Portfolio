/* Problem 1 University course enrollment */

/* Drop existing tables to prevent errors, just in case */

    DROP TABLE IF EXISTS enrollments;
    DROP TABLE IF EXISTS courses;
    DROP TABLE IF EXISTS professors;
    DROP TABLE IF EXISTS students;

/* students table */

    CREATE TABLE students (
        id SERIAL PRIMARY KEY,
        first_name VARCHAR(50),
        last_name VARCHAR(50),
        email VARCHAR(100),
        school_enrollment_date DATE
    );

/* professors table */

    CREATE TABLE professors (
        id SERIAL PRIMARY KEY,
        first_name VARCHAR(50),
        last_name VARCHAR(50),
        department VARCHAR(50)
    );

/* courses table */

    CREATE TABLE courses (
        id SERIAL PRIMARY KEY,
        course_name VARCHAR(50),
        course_description TEXT,
        professor_id INT REFERENCES professors(id)
    );

/* enrollments table */

    CREATE TABLE enrollments (
        student_id INT REFERENCES students(id),
        course_id INT REFERENCES courses(id),
        enrollment_date DATE,
        PRIMARY KEY (student_id, course_id)
    );

/* inserting some data */

    /* insert students */

        INSERT INTO students (first_name, last_name, email, school_enrollment_date)
        VALUES
        ('Alice', 'Johnson', 'alice123@gmail.com', '2025-09-01'),
        ('Bob', 'Smith', 'bob.smith@gmail.com', '2024-06-01'),
        ('Charlie', 'Brown', 'charliechoco@outlook.com', '2023-09-01'),
        ('Diana', 'Prince', 'dprincess@outlook.com', '2024-01-15'),
        ('Ethan', 'Hunt', 'ethan.hunt@example.com', '2023-04-10');

    /* insert professors */

        INSERT INTO professors (first_name, last_name, department)
        VALUES
        ('Jimbob', 'Maloney', 'Physics'),
        ('Alan', 'Boris', 'Computer Science'),
        ('Marie', 'Pearl', 'Chemistry'),
        ('Constance', 'Lovelace', 'Mathematics');

    /* insert courses */

        INSERT INTO courses (course_name, course_description, professor_id)
        VALUES
        (
            'Physics 101', 'Introduction to the fundamentals concepts of physics',
            (SELECT id FROM professors WHERE first_name = 'Jimbob' AND last_name = 'Maloney')
        ),
        (
            'Computer Science 101', 'Introduction to computer programming',
            (SELECT id FROM professors WHERE first_name = 'Alan' AND last_name = 'Boris')
        ),
        (
            'Chemistry 101', 'Basic principles of chemistry and lab work',
            (SELECT id FROM professors WHERE first_name = 'Marie' AND last_name = 'Pearl')
        ),
        (
            'Mathematics 101', 'Introduction to the principles of mathematics',
            (SELECT id FROM professors WHERE first_name = 'Constance' AND last_name = 'Lovelace')
        );

    /* insert enrollments */

        INSERT INTO enrollments (student_id, course_id, enrollment_date)
        VALUES
        (
            (SELECT id FROM students WHERE first_name = 'Alice' AND last_name = 'Johnson'),
            (SELECT id FROM courses WHERE course_name = 'Physics 101'),
            '2025-09-10'
        ),
        (
            (SELECT id FROM students WHERE first_name = 'Bob' AND last_name = 'Smith'),
            (SELECT id FROM courses WHERE course_name = 'Physics 101'),
            '2025-09-12'
        ),
        (
            (SELECT id FROM students WHERE first_name = 'Charlie' AND last_name = 'Brown'),
            (SELECT id FROM courses WHERE course_name = 'Computer Science 101'),
            '2025-09-15'
        ),
        (
            (SELECT id FROM students WHERE first_name = 'Diana' AND last_name = 'Prince'),
            (SELECT id FROM courses WHERE course_name = 'Chemistry 101'),
            '2025-10-01'
        ),
        (
            (SELECT id FROM students WHERE first_name = 'Ethan' AND last_name = 'Hunt'),
            (SELECT id FROM courses WHERE course_name = 'Computer Science 101'),
            '2025-10-05'
        );

/* SQL queries */

    /* retrive students in Physics */
        SELECT
        students.first_name || ' ' || students.last_name AS full_name
        FROM students
        JOIN enrollments ON students.id = enrollments.student_id
        JOIN courses ON enrollments.course_id = courses.id
        WHERE courses.course_name = 'Physics 101';

    /* update Email */

        UPDATE students
        SET email = 'bob.smith@cooluniversity.edu'
        WHERE first_name = 'Bob' AND last_name = 'Smith';

    /* delete a student from a course */

        DELETE FROM enrollments
        WHERE student_id = (
            SELECT id FROM students WHERE first_name = 'Bob' AND last_name = 'Smith'
        )
        AND course_id = (
            SELECT id FROM courses WHERE course_name = 'Physics 101'
        );

    /* some other stuff I used */

        /* update table constraint */

            ALTER TABLE courses
            ALTER COLUMN course_description TYPE TEXT;