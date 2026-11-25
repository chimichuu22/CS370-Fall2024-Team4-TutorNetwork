from database import get_connection

try:
    conn = get_connection()

    with conn.cursor() as cur:
        cur.execute("SELECT current_database();")
        print("Connected to:", cur.fetchone()[0])

        cur.execute("""
            SELECT COUNT(*)
            FROM information_schema.tables
            WHERE table_schema = 'public';
        """)
        print("Number of tables:", cur.fetchone()[0])

    conn.close()
    print("Supabase connection successful!")

except Exception as e:
    print("Connection failed:", e)
