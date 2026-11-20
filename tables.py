
def create_tables(conn):
    with conn.cursor() as cur:

        # TABLE 1: USERS
        cur.execute("""
            CREATE TABLE IF NOT EXISTS users (
                user_id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
                first_name VARCHAR(50) NOT NULL,
                last_name VARCHAR(50) NOT NULL,
                password VARCHAR(255) NOT NULL,
                role VARCHAR(10) NOT NULL
                    CHECK (role IN ('student', 'tutor'))
            );
        """)

            # TABLE 2: STUDENT
        cur.execute("""
            CREATE TABLE IF NOT EXISTS student (
                user_id INTEGER PRIMARY KEY
                    REFERENCES users(user_id),
                description TEXT
            );
         """)


            # TABLE 3: TUTOR
        cur.execute("""
            CREATE TABLE IF NOT EXISTS tutor (
                user_id INTEGER PRIMARY KEY
                    REFERENCES users(user_id),
                description TEXT,
                qualifications TEXT
            );
        """)

            # TABLE 4: COURSE
        cur.execute("""
            CREATE TABLE IF NOT EXISTS course (
                course_id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
                course_code VARCHAR(20) UNIQUE NOT NULL,
                course_name VARCHAR(100) NOT NULL,
                description TEXT
            );
        """)

            # TABLE 5: TUTOR_COURSE
        cur.execute("""
            CREATE TABLE IF NOT EXISTS tutor_course (
                tutor_id INTEGER NOT NULL
                    REFERENCES tutor(user_id),
                course_id INTEGER NOT NULL
                    REFERENCES course(course_id),
                PRIMARY KEY (tutor_id, course_id)
            );
        """)

            # TABLE 6: AVAILABILITY
        cur.execute("""
            CREATE TABLE IF NOT EXISTS availability (
                availability_id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
                tutor_id INTEGER NOT NULL,
                course_id INTEGER NOT NULL,
                available_date DATE NOT NULL,
                start_time TIME NOT NULL,
                end_time TIME NOT NULL,

                CHECK (end_time > start_time),

                FOREIGN KEY (tutor_id, course_id)
                    REFERENCES tutor_course(tutor_id, course_id)
            );
         """)

            # TABLE 7: SESSION_REQUEST
        cur.execute("""
            CREATE TABLE IF NOT EXISTS session_request (
                request_id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
                student_id INTEGER NOT NULL,
                availability_id INTEGER NOT NULL,
                status VARCHAR(15) NOT NULL DEFAULT 'Pending',
                requested_at TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
                message TEXT,

                FOREIGN KEY (student_id)
                    REFERENCES student(user_id),

                FOREIGN KEY (availability_id)
                     REFERENCES availability(availability_id)
            );
        """)

            # TABLE 8: FEEDBACK
        cur.execute("""
            CREATE TABLE IF NOT EXISTS feedback (
                feedback_id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
                request_id INTEGER NOT NULL UNIQUE,
                rating NUMERIC(2,1) NOT NULL
                    CHECK (rating BETWEEN 1 AND 5),
                comments TEXT,
                created_at TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,

                FOREIGN KEY (request_id)
                    REFERENCES session_request(request_id)
            );
        """)


    conn.commit()
