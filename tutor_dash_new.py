import streamlit as st

#configure the webpage
st.set_page_config(
    page_title = "Tutor Dashboard",
    page_icon = "📚",
    layout= "wide"
)

#configure sidebar navigation
with st.sidebar:
    st.sidebar.title("My Dashboard")
    #st.sidebar.write("---")

#buttons 
    st.button("Home", use_container_width = True)
    st.button("View Calendar", use_container_width = True)
    #st.button("Edit Calendar", use_container_width = True)
    st.button("Student Requests", use_container_width = True)
    st.button("Settings", use_container_width = True)

#main dashboard
st.title("Welcome to Tutor Network!")
st.write("Welcome back Tutor, here you can view your upcoming sessions, manage and edit requests. ")
st.write(" ")
