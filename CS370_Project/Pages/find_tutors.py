import streamlit as st

st.title("🔎 Find Tutors")

st.write("Search for tutors based on your course.")

search = st.text_input(
    "Search for a course",
    placeholder="Example: CS 370"
)

st.divider()

tutors = [
    {"name": "Emma", "course": "CS 370", "subject": "Computer Science"},
    {"name": "Alex", "course": "MATH 160", "subject": "Mathematics"},
    {"name": "John", "course": "PHYS 201", "subject": "Physics"}
]

st.subheader("Available Tutors")

for tutor in tutors:

    if search.lower() in tutor["course"].lower() or search == "":

        with st.container(border=True):
            st.subheader(tutor["name"])
            st.write("Course:", tutor["course"])
            st.write("Subject:", tutor["subject"])

            if st.button("View Profile", key=tutor["name"]):
                st.info("Tutor profile page coming soon")

# Sidebar navigation
with st.sidebar:
    st.title("🎓 TutorHub")
    st.write("Your campus tutoring network")
    st.divider()

    st.subheader("Navigation")

    if st.button("🏠 Home", use_container_width=True):
        st.switch_page("app.py")

    if st.button("🔎 Find Tutors", use_container_width=True):
        st.switch_page("pages/find_tutors.py")

    if st.button("📚 Student Dashboard", use_container_width=True):
        st.switch_page("pages/student_dashboard.py")

    if st.button("👩‍🏫 Tutor Dashboard", use_container_width=True):
        st.switch_page("pages/tutor_dashboard.py")