import streamlit as st



def wallpaper():
    st.markdown("""
    <style>
    .stApp {
        background-color: #CCF0F1;
    }
    </style>
    """, unsafe_allow_html=True)

    st.title("Hello, Student!")

    st.write("Major:")


    tab1, tab2,tab3 = st.tabs(["Requested session", "Past sessions", "upcoming session"])

    with tab1:
        st.markdown("""
            <div style="background-color: white;
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
            <div style="background-color: white;
                    padding: 20px;
                    border-radius: 10px;
                    color: #17324D;">
            <h4>Requested Session</h4>
            <p>Tutor: name</p>
            <p>Course: CS 370</p>
            <p>Status: Past sessions</p>
        </div>
        """, unsafe_allow_html=True)
    with tab3:
        st.markdown("""
            <div style="background-color: white;
                    padding: 20px;
                    border-radius: 10px;
                    color: #17324D;">
            <h4>Requested Session</h4>
            <p>Tutor: name</p>
            <p>Course: CS 370</p>
            <p>Status: upcoming</p>
        </div>
        """, unsafe_allow_html=True)


def features():

    st.markdown("""
        <style>
        [data-testid="stSidebar"] {background-color: #87CEEB; }
    </style>
""", unsafe_allow_html=True)

    
    st.divider()

    st.header("My Courses")
    st.write("Current Courses: CS 211, CS 370")

    with st.sidebar:
    
        st.title("Tutor Hub")
        st.divider()
        

        a = st.sidebar.text_input("Search for Course related tutors: ")

        st.button("Home")
        st.button("Find a Tutor")
    
        st.button("My Sessions")
        st.button("feedback")

        st.divider()

        st.button("settings")
        st.button("Log out")


wallpaper()

features()

    





