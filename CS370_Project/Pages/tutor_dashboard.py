
import streamlit as st
from datetime import datetime
from session_store import requests

st.title("Welcome to Tutor Hub!")

st.write(
    "Welcome back Tutor, here you can view your "
    "upcoming sessions and manage your courses."
)

st.divider()

st.header("My Dashboard")

# ------------------------------------------
# Publish Courses & Availability
# ------------------------------------------

if st.button(
    "📚 Publish Courses & Availability",
    use_container_width=True,
    type="primary"
):
    st.switch_page("pages/publish_courses.py")

st.divider()

# ------------------------------------------
# Upcoming Sessions
# ------------------------------------------

st.subheader("Upcoming Sessions")

upcoming = [
    item for item in requests()
    if item["status"] == "Accepted"
    and item["when"] >= datetime.now()
]

if not upcoming:
    st.info("No upcoming sessions.")

for item in upcoming:
    with st.container(border=True):

        st.write("Student:", item["student"])
        st.write("Course:", item["course"])

        st.write(
            "Date:",
            item["when"].strftime("%m/%d/%Y")
        )

        st.write(
            "Time:",
            item["when"].strftime("%I:%M %p")
        )

        st.write("Status: Upcoming")

st.divider()

# ------------------------------------------
# Sidebar Navigation
# ------------------------------------------

with st.sidebar:

    st.title("🎓 TutorHub")
    st.divider()

    if st.button(
        "🏠 Home",
        use_container_width=True
    ):
        st.switch_page("app.py")

    if st.button(
        "📚 Publish Courses",
        use_container_width=True
    ):
        st.switch_page("pages/publish_courses.py")

    if st.button(
        "📩 Student Requests",
        use_container_width=True
    ):
        st.switch_page("pages/student_requests.py")


    if st.button(
        "View Calendar",
        use_container_width=True
    ):
        st.info("Calendar coming soon")

    if st.button(
        "Settings",
        use_container_width=True
    ):
        st.info("Settings coming soon")

    if st.button(
        "Logout",
        use_container_width=True
    ):
        st.info("Login/logout will be added later")
