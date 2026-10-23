
import streamlit as st

st.set_page_config(
    page_title="TutorHub",
    page_icon="🎓",
    layout="wide"
)

# Simple CSS for the home page
st.markdown("""
<style>
.block-container {
    max-width: 1100px;
    padding-top: 2rem;
}

.welcome-box {
    background-color: #EFF6FF;
    padding: 35px;
    border-radius: 15px;
    text-align: center;
    margin-bottom: 25px;
}

.welcome-box h1 {
    color: #1E3A8A;
    font-size: 42px;
}

.welcome-box p {
    color: #475569;
    font-size: 18px;
}
</style>
""", unsafe_allow_html=True)


# Navigation sidebar
with st.sidebar:
    st.title("🎓 TutorHub")
    st.write("Your campus tutoring network")
    st.divider()

    st.subheader("Navigation")

    if st.button("🔎 Find Tutors", use_container_width=True):
        st.switch_page("pages/find_tutors.py")

    if st.button("📚 Student Dashboard", use_container_width=True):
        st.switch_page("pages/student_dashboard.py")

    if st.button("👩‍🏫 Tutor Dashboard", use_container_width=True):
        st.switch_page("pages/tutor_dashboard.py")


# Welcome section
st.markdown("""
<div class="welcome-box">
    <h1>Welcome to TutorHub 🎓</h1>
    <p>
        Connect with tutors, get academic support,
        and achieve your learning goals.
    </p>
</div>
""", unsafe_allow_html=True)


# Mission section
st.subheader("Our Mission")

st.write(
    "TutorHub is a campus-based platform designed "
    "to help students connect with tutors. Students can "
    "search for tutors based on their courses, while tutors "
    "can share their knowledge and help others succeed."
)

st.divider()



# Student and Tutor sections
st.subheader("Get Started")

col1, col2 = st.columns(2, gap="large")

# For Students
with col1:
    with st.container(border=True):
        st.header("📚 For Students")

        st.write(
            "Find tutors for your courses, explore tutor "
            "profiles, and get academic help."
        )

        student_login, student_register = st.columns(2)

        with student_login:
            if st.button(
                "Login",
                key="student_login",
                use_container_width=True,
                type="primary"
            ):
                st.session_state["selected_role"] = "Student"
                st.switch_page("pages/login.py")

        with student_register:
            if st.button(
                "Register",
                key="student_register",
                use_container_width=True
            ):
                st.session_state["selected_role"] = "Student"
                st.switch_page("pages/register.py")


# For Tutors
with col2:
    with st.container(border=True):
        st.header("👩‍🏫 For Tutors")

        st.write(
            "Help other students, manage tutoring "
            "requests, and organize your sessions."
        )

        tutor_login, tutor_register = st.columns(2)

        with tutor_login:
            if st.button(
                "Login",
                key="tutor_login",
                use_container_width=True,
                type="primary"
            ):
                st.session_state["selected_role"] = "Tutor"
                st.switch_page("pages/login.py")

        with tutor_register:
            if st.button(
                "Register",
                key="tutor_register",
                use_container_width=True
            ):
                st.session_state["selected_role"] = "Tutor"
                st.switch_page("pages/register.py")


st.divider()

# How the platform works
st.subheader("How It Works?")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("### 🔎 Search")
    st.write("Find tutors for your courses.")

with col2:
    st.markdown("### 📅 Connect")
    st.write("Send tutoring requests.")

with col3:
    st.markdown("### 🎓 Learn")
    st.write("Get academic support and improve your skills.")

st.divider()
st.caption("TutorHub | Campus Tutoring Network")
