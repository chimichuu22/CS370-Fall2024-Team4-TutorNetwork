import streamlit as st
import datetime 

st.title("🔎 Find Tutors")

st.write("Search for tutors based on your course.")

#store selected tutor and tutoring requests
if "selected_tutor" not in st.session_state:
    st.session_state.selected_tutor = None
if "pending_requests" not in st.session_state:
    st.session_state.pending_requests = set()
if "last_requested" not in st.session_state:
    st.session_state.last_requested = None

search = st.text_input(
    "Search for a course",
    placeholder="Example: CS 370"
)

date_op = st.date_input("Pick a date", value=None)
time_op = st.time_input("Pick a time", value=None, format="12h")

#available tutors with details about them 
tutors = [
    {
        "name": "Emma",
        "course": "CS 370",
        "subject": "Computer Science",
        "Date": datetime.date(2027, 4, 20),
        "time": datetime.time(15, 30),
        "description": "Computer Science tutor with experience in programming and software development.",
        "rating": "⭐⭐⭐⭐⭐"
    },
    {
        "name": "Alex",
        "course": "MATH 160",
        "subject": "Mathematics",
        "Date": datetime.date(2027, 4, 30),
        "time": datetime.time(16, 30),
        "description": "Mathematics tutor specializing in algebra and calculus.",
        "rating": "⭐⭐⭐⭐⭐"
    },
    {
        "name": "John",
        "course": "PHYS 201",
        "subject": "Physics",
        "Date": datetime.date(2027, 5, 6),
        "time": datetime.time(17, 30),
        "description": "Physics tutor who enjoys helping others understand difficult concepts.",
        "rating": "⭐⭐⭐⭐⭐"
    }
]

#create a unique ID for each tutor
def tutor_id(tutor):
    return f"{tutor['name']}_{tutor['course']}_{tutor['Date']}_{tutor['time']}"

st.divider()

#tutor profile page 
if st.session_state.selected_tutor is not None:
    selected = next(
        t for t in tutors
        if tutor_id(t) == st.session_state.selected_tutor
    )

    st.subheader("👩‍🏫 Tutor Profile")

    if st.button("← Back to Find Tutors"):
        st.session_state.selected_tutor = None
        st.rerun()

    st.divider()

    st.header(selected["name"])

    st.write("**Subject:**", selected["subject"])
    st.write("**Course:**", selected["course"])
    st.write("**Rating:**", selected["rating"])
    st.write("**About Me:**", selected["description"])

    st.divider()

    st.subheader("📅 Available Tutoring Session")
    st.write(
        "Date:",
        selected["Date"].strftime("%m/%d/%Y")
    )
    st.write(
        "Time:",
        selected["time"].strftime("%I:%M %p")
    )
    current_id = tutor_id(selected)

    #check whether a request already exists
    if current_id in st.session_state.pending_requests:
        st.warning("⏳ Request Status: PENDING")
        st.write(
            "Your tutoring request has been submitted "
            "and is waiting for the tutor's response."
        )

    else:

        if st.button("📨 Request Tutoring Session", type="primary"):
            st.session_state.pending_requests.add(current_id)
            st.session_state.last_requested = current_id
            st.rerun()

    #show confirmation after submitting
    if st.session_state.last_requested == current_id:
        st.success("Your tutoring request was successfully submitted!")


#tutor search page 
else:
    st.subheader("Available Tutors")

    found = False

    for tutor in tutors:

        current_id = tutor_id(tutor)

        # Apply search filters
        if (
            (search.lower() in tutor["course"].lower() or search == "")
            and (date_op is None or date_op == tutor["Date"])
            and (time_op is None or time_op == tutor["time"])
        ):

            found = True

            with st.container(border=True):

                st.subheader(tutor["name"])

                st.write("Date available:", tutor["Date"].strftime("%m/%d/%Y"))
                st.write("Time available:", tutor["time"].strftime("%I:%M %p"))
                st.write("Course:", tutor["course"])
                st.write("Subject:", tutor["subject"])

                # Display request status
                if current_id in st.session_state.pending_requests:
                    st.warning("⏳ PENDING")

                if st.button(
                    "View Profile",
                    key=f"profile_{current_id}"
                ):

                    st.session_state.selected_tutor = current_id
                    st.rerun()

    if not found:
        st.subheader(
            "Sorry! No tutor is available for this time or course."
        )

#sidebar navigation
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