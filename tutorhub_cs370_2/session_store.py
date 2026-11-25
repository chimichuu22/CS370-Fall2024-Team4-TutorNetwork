
"""Database storage for TutorHub."""

import datetime
import streamlit as st
import psycopg2
import psycopg2.extras

from database import get_connection


# Temporary ID for testing without a login system.
# This ID must exist in the student table.
DEMO_STUDENT_ID = 7


# --------------------------------------------------
# GET ALL AVAILABLE TUTOR SLOTS
# --------------------------------------------------

def slots():

    conn = get_connection()

    try:
        with conn.cursor(
            cursor_factory=psycopg2.extras.RealDictCursor
        ) as cur:

            cur.execute("""
                SELECT
                    a.availability_id AS id,
                    a.tutor_id,
                    a.course_id,
                    a.available_date AS "Date",
                    a.start_time AS time,
                    a.end_time,
                    u.full_name AS name,
                    t.description,
                    t.qualifications,
                    c.course_code AS course,
                    c.course_name AS subject

                FROM availability a

                JOIN tutor t
                    ON a.tutor_id = t.user_id

                JOIN users u
                    ON t.user_id = u.user_id

                JOIN course c
                    ON a.course_id = c.course_id

                WHERE u.role = 'tutor'

                ORDER BY a.available_date, a.start_time
            """)

            results = [dict(row) for row in cur.fetchall()]

            for slot in results: #keep the same keys the page expects
                slot["rating"] = "New tutor"

            return results

    finally:
        conn.close()


# --------------------------------------------------
# GET ALL TUTORING REQUESTS
# --------------------------------------------------

def requests():

    conn = get_connection()

    try:
        with conn.cursor(
            cursor_factory=psycopg2.extras.RealDictCursor
        ) as cur:

            cur.execute("""
                SELECT
                    sr.request_id AS id,
                    sr.availability_id AS slot_id,
                    sr.student_id,
                    sr.status,
                    sr.requested_at,
                    sr.message,

                    su.full_name AS student,
                    tu.full_name AS tutor,

                    c.course_code AS course,
                    a.available_date AS "Date",
                    a.start_time AS time

                FROM session_request sr

                JOIN student s
                    ON sr.student_id = s.user_id

                JOIN users su
                    ON s.user_id = su.user_id

                JOIN availability a
                    ON sr.availability_id = a.availability_id

                JOIN tutor t
                    ON a.tutor_id = t.user_id

                JOIN users tu
                    ON t.user_id = tu.user_id

                JOIN course c
                    ON a.course_id = c.course_id

                ORDER BY sr.requested_at DESC
            """)

            results = [dict(row) for row in cur.fetchall()]

            for request in results: #create the datetime value expected by the pages
                request["when"] = datetime.datetime.combine(
                    request["Date"],
                    request["time"]
                )

            return results

    finally:
        conn.close()


# --------------------------------------------------
# PUBLISH A TUTOR'S AVAILABILITY
# --------------------------------------------------

def publish(name, course, date, time, description):

    name = name.strip()
    course = course.strip().upper()

    if not name or not course:
        return False, "Tutor name and course are required."

    if date < datetime.date.today():
        return False, "Choose a future date."

    start_time = time #temporarily create each session one hour long
    end_time = (
        datetime.datetime.combine(date, time)
        + datetime.timedelta(hours=1)
    ).time()

    conn = get_connection()

    try:
        with conn.cursor() as cur:
            #find the tutor using their name
            cur.execute(""" 
                SELECT t.user_id
                FROM tutor t
                JOIN users u ON t.user_id = u.user_id
                WHERE LOWER(u.full_name) = LOWER(%s)
                  AND u.role = 'tutor'
            """, (name,))

            tutor = cur.fetchone()

            if tutor is None:
                return False, "Tutor was not found in the database."

            tutor_id = tutor[0]

            #find the course using its course code
            cur.execute("""
                SELECT course_id
                FROM course
                WHERE UPPER(course_code) = %s
            """, (course,))

            course_result = cur.fetchone()

            if course_result is None:
                return False, "Course was not found in the database."

            course_id = course_result[0]

            #check for an existing availability at this time
            cur.execute("""
                SELECT availability_id
                FROM availability
                WHERE tutor_id = %s
                  AND course_id = %s
                  AND available_date = %s
                  AND start_time = %s
            """, (tutor_id, course_id, date, start_time))

            if cur.fetchone():
                return False, "This course and time are already published."

            #make sure the tutor is associated with this course
            cur.execute("""
                INSERT INTO tutor_course (tutor_id, course_id)
                VALUES (%s, %s)
                ON CONFLICT (tutor_id, course_id) DO NOTHING
            """, (tutor_id, course_id))

            #insert the new availability
            cur.execute("""
                INSERT INTO availability (
                    tutor_id,
                    course_id,
                    available_date,
                    start_time,
                    end_time
                )
                VALUES (%s, %s, %s, %s, %s)
            """, (
                tutor_id,
                course_id,
                date,
                start_time,
                end_time
            ))

        conn.commit()

        return True, "Course and availability published!"

    except Exception as e:
        conn.rollback()
        return False, f"Unable to publish availability: {e}"

    finally:
        conn.close()


# --------------------------------------------------
# SUBMIT A TUTORING REQUEST
# --------------------------------------------------

def submit(slot, student_name):

    conn = get_connection()

    try:
        with conn.cursor() as cur:

            #check whether this slot already has a Pending or Accepted request from this student
            cur.execute("""
                SELECT request_id
                FROM session_request
                WHERE availability_id = %s
                  AND student_id = %s
                  AND status IN ('Pending', 'Accepted')
            """, (slot["id"], DEMO_STUDENT_ID))

            if cur.fetchone():
                return False, "This slot already has an active request."

            #make sure the demo student exists
            cur.execute("""
                SELECT user_id
                FROM student
                WHERE user_id = %s
            """, (DEMO_STUDENT_ID,))

            if cur.fetchone() is None:
                return False, (
                    "Demo student ID does not exist. "
                    "Check the student table."
                )

            #insert the tutoring request
            cur.execute("""
                INSERT INTO session_request (
                    student_id,
                    availability_id,
                    status,
                    requested_at
                )
                VALUES (%s, %s, %s, CURRENT_TIMESTAMP)
            """, (
                DEMO_STUDENT_ID,
                slot["id"],
                "Pending"
            ))

        conn.commit()

        return True, "Request submitted with Pending status."

    except Exception as e:
        conn.rollback()
        return False, f"Unable to submit request: {e}"

    finally:
        conn.close()


# --------------------------------------------------
# ACCEPT OR DECLINE A TUTORING REQUEST
# --------------------------------------------------

def decide(request_id, status):

    if status not in ("Accepted", "Declined"):
        return False

    conn = get_connection()

    try:
        with conn.cursor() as cur:

            cur.execute("""
                UPDATE session_request
                SET status = %s
                WHERE request_id = %s
                  AND status = 'Pending'
            """, (status, request_id))

            updated = cur.rowcount

        conn.commit()

        return updated > 0

    except Exception:
        conn.rollback()
        return False

    finally:
        conn.close()
