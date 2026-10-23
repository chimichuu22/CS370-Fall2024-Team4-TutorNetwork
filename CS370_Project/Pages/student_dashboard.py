import streamlit as st

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

    tab1, tab2, tab3 = st.tabs([
        "Requested session",
        "Past sessions",
        "Upcoming session"
    ])

    with tab1:
        st.markdown("""
        <div style="background-color: #F3F6FB;
            padding: 20px;
            border-radius: 10px;
            color: #17324D;">
            <h4>Requested Session</h4>
            <p>Tutor: name</p>
            <p>Course: CS 370</p>
            <p>Status: Pending</p>
        </div>
        """, unsafe_allow_html=True)

    with tab2:
        st.markdown("""
        <div style="background-color: #F3F6FB;
            padding: 20px;
            border-radius: 10px;
            color: #17324D;">
            <h4>Past Session</h4>
            <p>Tutor: name</p>
            <p>Course: CS 370</p>
            <p>Status: Completed</p>
        </div>
        """, unsafe_allow_html=True)

    with tab3:
        st.markdown("""
        <div style="background-color: #F3F6FB;
            padding: 20px;
            border-radius: 10px;
            color: #17324D;">
            <h4>Upcoming Session</h4>
            <p>Tutor: name</p>
            <p>Course: CS 370</p>
            <p>Status: Upcoming</p>
        </div>
        """, unsafe_allow_html=True)


def features():
    st.divider()

    st.header("My Courses")
    st.write("Current Courses: CS 211, CS 370, MATH 162")

    with st.sidebar:
        st.title("Tutor Hub")
        st.divider()

        if st.button("Home", use_container_width=True):
            st.switch_page("app.py")

        if st.button("Find a Tutor", use_container_width=True):
            st.switch_page("pages/find_tutors.py")

        if st.button("My Sessions", use_container_width=True):
            st.info("My Sessions page coming soon")

        if st.button("Feedback", use_container_width=True):
            st.info("Feedback feature coming soon")

        st.divider()

        if st.button("Settings", use_container_width=True):
            st.info("Settings coming soon")

        if st.button("Log out", use_container_width=True):
            st.info("Login/logout will be added later")


wallpaper()
features()