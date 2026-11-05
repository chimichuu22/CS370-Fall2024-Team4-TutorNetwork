
import streamlit as st
from datetime import datetime
from session_store import requests


def show_session(item):
    with st.container(border=True):
        st.write("Tutor:", item["tutor"])
        st.write("Course:", item["course"])
        st.write(
            "Date:",
            item["when"].strftime("%m/%d/%Y")
        )
        st.write(
            "Time:",
            item["when"].strftime("%I:%M %p")
        )
        st.write("Status:", item["status"])


def wallpaper():
    st.markdown("""
    <style>
    .stApp {
        background-color: #FFFFFF;
    }
    </style>
    """, unsafe_allow_html=True)

    st.title("Hello, Student!")
    st.write("Major: Computer Science")

    all_requests = requests()

    tab1, tab2, tab3 = st.tabs([
        "Requested session",
        "Past sessions",
        "Upcoming session"
    ])

    # Requested sessions
    with tab1:
        st.subheader("Requested Sessions")

        pending = [
            item for item in all_requests
            if item["status"] == "Pending"
        ]

        if not pending:
            st.info("No pending tutoring requests.")

        for item in pending:
            show_session(item)

    # Past sessions
    with tab2:
        st.subheader("Past Sessions")

        past = [
            item for item in all_requests
            if item["status"] == "Completed"
            or (
                item["status"] == "Accepted"
                and item["when"] < datetime.now()
            )
        ]

        if not past:
            st.info("No past tutoring sessions.")

        for item in past:
            show_session(item)

    # Upcoming sessions
    with tab3:
        st.subheader("Upcoming Sessions")

        upcoming = [
            item for item in all_requests
            if item["status"] == "Accepted"
            and item["when"] >= datetime.now()
        ]

        if not upcoming:
            st.info("No upcoming tutoring sessions.")

        for item in upcoming:
            show_session(item)


def features():
    st.divider()

    st.header("My Courses")
    st.write("Current Courses: CS 211, CS 370, MATH 162")

    with st.sidebar:
        st.title("Tutor Hub")
        st.divider()

        if st.button("Home", use_container_width=True):
            st.switch_page("app.py")

        if st.button(
            "Find a Tutor",
            use_container_width=True
        ):
            st.switch_page("pages/find_tutors.py")



        if st.button("Feedback", use_container_width=True):
            st.info("Feedback feature coming soon")

        st.divider()

        if st.button("Settings", use_container_width=True):
            st.info("Settings coming soon")

        if st.button("Log out", use_container_width=True):
            st.info("Login/logout will be added later")


wallpaper()
features()

# Show declined requests separately
declined = [
    item for item in requests()
    if item["status"] == "Declined"
]

if declined:
    st.divider()
    st.subheader("Declined Requests")

    for item in declined:
        show_session(item)
