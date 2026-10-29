import streamlit as st
import datetime

st.title("🔎 Find Tutors")

st.write("Search for tutors based on your course.")

search = st.text_input(
    "Search for a course",
    placeholder="Example: CS 370"
)


date_op = st.date_input("pick a date", value= None)
time_op = st.time_input("pick a time",value = None, format = "12h")


st.divider()

tutors = [
    {"name": "Emma", "course": "CS 370", "subject": "Computer Science","Date": datetime.date(2027,4,20),"time": datetime.time(15,30)},
    {"name": "Alex", "course": "MATH 160", "subject": "Mathematics", "Date": datetime.date(2027,4,30),"time": datetime.time(16,30)},
    {"name": "John", "course": "PHYS 201", "subject": "Physics","Date": datetime.date(2027,5,6),"time": datetime.time(17,30)}
]


st.subheader("Available Tutors")


found = False

for tutor in tutors:


        if (search.lower() in tutor["course"].lower() or search == "") and (time_op is None or time_op == tutor["time"]) and (date_op is None or date_op == tutor["Date"]):
            found = True

            with st.container(border=True):
                st.subheader(tutor["name"])

                st.write("Date available:", tutor["Date"].strftime("%m/ %d/ %Y"))

                st.write("Time available:", tutor["time"].strftime("%I:%M %p"))
           

                st.write("Course:", tutor["course"])
                st.write("Subject:", tutor["subject"])

                if st.button("View Profile", key= f"{tutor["name"]}_{tutor['Date']}_{tutor['time']}"):
                    st.info("Tutor profile page coming soon")

if not found:
    st.subheader("Sorry! No tutor is available for this time or course")
    
#--------------------------------------------------------------------------------------------

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
        

