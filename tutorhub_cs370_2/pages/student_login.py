
import streamlit as st


st.markdown("""
    <style>
        [data-testid="stSidebar"] {
            display: none;
        }
    </style>
""", unsafe_allow_html=True)


col1, col2, col3 = st.columns([2, 7, 2])
with col2:
    st.title("Student Login")
    
    with st.container(border=True):
        st.subheader("Sign in")

        email = st.text_input("Email", placeholder="Enter your email")

        password = st.text_input(
            "Password",
            type="password",
            placeholder="Enter your password"
        )

        button1,button2, button3 = st.columns([2,3,2])

        with button2:
            if st.button("Login", use_container_width=True):
                if email  == "fake@gmail.com" and password == "fake" :
                    st.success("Login information entered!")
                    st.switch_page("pages/student_dashboard.py")

                elif email == "" or password == "":
                    st.error("please fill in both username and password")

                elif email  != "fake@gmail.com" and password != "fake" :
                    st.error("password or username is incorrect")

            if st.button("Need an Account?", use_container_width=True):
                st.switch_page("pages/student_reg.py")

button4,button5,button6 = st.columns([2, 3, 2])

with button5:
    if st.button("Home", use_container_width=True):
        st.switch_page("app.py")