
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
    st.title("Tutor Registration")
    
    with st.container(border=True):
        st.subheader("Sign Up")

        email = st.text_input("Email", placeholder="Enter your email")

        password = st.text_input(
            "Password",
            type="password",
            placeholder="Enter your password"
        )

        button1,button2, button3 = st.columns([2,3,2])
        with button2:
            if st.button("register", use_container_width=True):
                if email  != "" and password != "":
                    st.success("You've been registered! Please go Login")

                elif email == email or password == password:
                    st.error("please fill in both username and password")

       

            if st.button("Have an Account?", use_container_width=True):
                st.switch_page("pages/tutor_login.py")


button4,button5,button6 = st.columns([2, 3, 2])

with button5:
    if st.button("Home", use_container_width=True):
        st.switch_page("app.py")