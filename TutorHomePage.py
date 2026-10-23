import streamlit as st

col1, col2,col3 = st.columns(3)

with col1:
    st.title("Tutor Hub")
    st.write("Welcome to the Tutor Hub")

with col2:
    st.header("Tutoring Hub")
    st.subheader("Our mission")
    st.text("Create an environment for students to connect with tutors")


with col3:
#in future add on_click
    if st.button("Login"):
        st.write("taking to log in")
    # vvv this might allow to move to other pages
    #st.switch_page("pages/LoginPage.py")
    if st.button("Sign up"):
        st.write("taking to sign up")
    #st.switch_page("pages/SignUpPage.py")


st.sidebar.title("Where would you like to go?")
st.markdown("Sessions")
st.markdown("Account")
st.markdown("Log out")