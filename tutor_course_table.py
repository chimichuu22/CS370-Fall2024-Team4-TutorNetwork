def create_tutor_course_tables(conn):
    with conn.cursor() as cur:

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
