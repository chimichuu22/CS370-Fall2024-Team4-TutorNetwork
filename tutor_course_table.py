-- TABLE 3: TUTOR
CREATE TABLE IF NOT EXISTS tutor (
    user_id INTEGER PRIMARY KEY,
    description TEXT,
    qualifications TEXT,

    FOREIGN KEY (user_id)
        REFERENCES users(user_id)
);

-- TABLE 4: COURSE
CREATE TABLE IF NOT EXISTS course (
    course_id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    course_code VARCHAR(20) UNIQUE NOT NULL,
    course_name VARCHAR(100) NOT NULL,
    description TEXT
);

-- TABLE 5: TUTOR_COURSE
CREATE TABLE IF NOT EXISTS tutor_course (
    tutor_id INTEGER NOT NULL,
    course_id INTEGER NOT NULL,

    PRIMARY KEY (tutor_id, course_id),

    FOREIGN KEY (tutor_id)
        REFERENCES tutor(user_id),

    FOREIGN KEY (course_id)
        REFERENCES course(course_id)
);