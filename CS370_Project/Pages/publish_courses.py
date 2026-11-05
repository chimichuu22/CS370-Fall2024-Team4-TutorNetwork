
import datetime
import streamlit as st
from session_store import publish, slots

st.title("📚 Publish Courses & Availability")

st.write(
    "Add the courses you can teach and publish "
    "your available tutoring dates and times."
)

st.divider()

# Form for publishing courses
with st.form("publish_course_form"):

    tutor_name = st.text_input(
        "Tutor Name",
        placeholder="Enter your name"
    )

    course = st.text_input(
        "Course",
        placeholder="Example: CS 370"
    )

    available_date = st.date_input(
        "Available Date",
        value=datetime.date.today()
    )

    available_time = st.time_input(
        "Available Time",
        value=datetime.time(15, 0)
    )

    description = st.text_area(
        "About Me (Optional)",
        placeholder="Describe your tutoring experience"
    )

    submitted = st.form_submit_button(
        "Publish Course & Availability",
        type="primary"
    )

if submitted:
    success, message = publish(
        tutor_name,
        course,
        available_date,
        available_time,
        description
    )

    if success:
        st.success(message)
    else:
        st.warning(message)

st.divider()

# Show published courses
st.subheader("My Published Courses")

published = slots()

if not published:
    st.info("No courses have been published yet.")

for slot in published:
    with st.container(border=True):
        st.write("**Tutor:**", slot["name"])
        st.write("**Course:**", slot["course"])

        st.write(
            "**Date:**",
            slot["Date"].strftime("%m/%d/%Y")
        )

        st.write(
            "**Time:**",
            slot["time"].strftime("%I:%M %p")
        )

st.divider()

if st.button("⬅ Back to Tutor Dashboard"):
    st.switch_page("pages/tutor_dashboard.py")

# Sidebar navigation
with st.sidebar:
    st.title("🎓 TutorHub")
    st.divider()

    if st.button("🏠 Home", use_container_width=True):
        st.switch_page("app.py")

    if st.button(
        "👩‍🏫 Tutor Dashboard",
        use_container_width=True
    ):
        st.switch_page("pages/tutor_dashboard.py")

    if st.button(
        "🔎 Find Tutors",
        use_container_width=True
    ):
        st.switch_page("pages/find_tutors.py")
