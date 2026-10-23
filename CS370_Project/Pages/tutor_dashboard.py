import streamlit as st

st.title("Welcome to Tutor Hub!")

st.write(
    "Welcome back Tutor, here you can view your "
    "upcoming sessions, manage and edit requests."
)

st.divider()

st.header("My Dashboard")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Upcoming Sessions")

    with st.container(border=True):
        st.write("Student: name")
        st.write("Course: CS 370")
        st.write("Date: TBD")
        st.write("Status: Upcoming")

with col2:
    st.subheader("Student Requests")

    with st.container(border=True):
        st.write("Student: name")
        st.write("Course: CS 211")
        st.write("Status: Pending")

st.divider()

with st.sidebar:
    st.title("My Dashboard")
    st.divider()

    if st.button("Home", use_container_width=True):
        st.switch_page("app.py")

    if st.button("View Calendar", use_container_width=True):
        st.info("Calendar coming soon")

    if st.button("Student Requests", use_container_width=True):
        st.info("Student request management coming soon")

    if st.button("Settings", use_container_width=True):
        st.info("Settings coming soon")
        
    if st.button("Logout",use_container_width=True):
        st.info("To logout")