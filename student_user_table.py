def create_student_user_tables(conn):
    with conn.cursor() as cur:

        # TABLE 1: USER
        cur.execute("""
            CREATE TABLE IF NOT EXISTS user (
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