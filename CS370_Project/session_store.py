
"""Temporary storage for TutorHub Sprint 2."""

import datetime
import streamlit as st
from StudentTutorClasses import Student, Tutor


def initialize():
    if "tutor_slots" not in st.session_state:
        st.session_state.tutor_slots = [
            {
                "id": "emma-cs370",
                "name": "Emma",
                "course": "CS 370",
                "subject": "Computer Science",
                "Date": datetime.date(2027, 4, 20),
                "time": datetime.time(15, 30),
                "description": "Computer Science tutor with experience in programming and software development.",
                "rating": "⭐⭐⭐⭐⭐"
            },
            {
                "id": "alex-math160",
                "name": "Alex",
                "course": "MATH 160",
                "subject": "Mathematics",
                "Date": datetime.date(2027, 4, 30),
                "time": datetime.time(16, 30),
                "description": "Mathematics tutor specializing in algebra and calculus.",
                "rating": "⭐⭐⭐⭐⭐"
            },
            {
                "id": "john-phys201",
                "name": "John",
                "course": "PHYS 201",
                "subject": "Physics",
                "Date": datetime.date(2027, 5, 6),
                "time": datetime.time(17, 30),
                "description": "Physics tutor who enjoys helping others understand difficult concepts.",
                "rating": "⭐⭐⭐⭐⭐"
            }
        ]

    if "tutoring_requests" not in st.session_state:
        st.session_state.tutoring_requests = []


def slots():
    initialize()
    return st.session_state.tutor_slots


def requests():
    initialize()
    return st.session_state.tutoring_requests


def publish(name, course, date, time, description):
    name = name.strip()
    course = course.strip().upper()

    if not name or not course:
        return False, "Tutor name and course are required."

    if date < datetime.date.today():
        return False, "Choose a future date."

    for slot in slots():
        if (
            slot["name"].casefold() == name.casefold()
            and slot["course"] == course
            and slot["Date"] == date
            and slot["time"] == time
        ):
            return False, "This course and time are already published."

    next_id = st.session_state.get("next_slot_id", 1)
    st.session_state.next_slot_id = next_id + 1

    slots().append({
        "id": f"published-{next_id}",
        "name": name,
        "course": course,
        "subject": course,
        "Date": date,
        "time": time,
        "description": description.strip() or "Tutor available to help with this course.",
        "rating": "New tutor"
    })

    return True, "Course and availability published!"


def submit(slot, student_name):
    for request in requests():
        if (
            request["slot_id"] == slot["id"]
            and request["status"] in ("Pending", "Accepted")
        ):
            return False, "This slot already has an active request."

    student = Student(
        student_name.strip() or "Demo Student",
        [slot["course"]]
    )

    tutor = Tutor(slot["name"], [slot["course"]])

    when = datetime.datetime.combine(
        slot["Date"], slot["time"]
    )

    session = student.request_session(
        tutor, slot["course"], when
    )

    if session is None:
        return False, "Unable to create request."

    next_id = st.session_state.get("next_request_id", 1)
    st.session_state.next_request_id = next_id + 1

    requests().append({
        "id": next_id,
        "slot_id": slot["id"],
        "student": student.name,
        "tutor": tutor.name,
        "course": slot["course"],
        "when": when,
        "status": session.status
    })

    return True, "Request submitted with Pending status."


def decide(request_id, status):
    if status not in ("Accepted", "Declined"):
        return False

    for request in requests():
        if (
            request["id"] == request_id
            and request["status"] == "Pending"
        ):
            request["status"] = status
            return True

    return False
