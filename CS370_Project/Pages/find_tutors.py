
import streamlit as st
from session_store import slots, requests, submit

st.title("🔎 Find Tutors")
st.write("Search for tutors based on your course.")

if "selected_tutor" not in st.session_state:
    st.session_state.selected_tutor = None

search = st.text_input(
    "Search for a course",
    placeholder="Example: CS 370"
)

date_op = st.date_input("Pick a date", value=None)
time_op = st.time_input(
    "Pick a time",
    value=None,
    format="12h"
)

st.divider()

selected = next(
    (
        tutor for tutor in slots()
        if tutor["id"] == st.session_state.selected_tutor
    ),
    None
)

# Tutor profile
if selected:
    st.subheader("👩‍🏫 Tutor Profile")

    if st.button("← Back to Find Tutors"):
        st.session_state.selected_tutor = None
        st.rerun()

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

    active = next(
        (
            request for request in requests()
            if request["slot_id"] == selected["id"]
            and request["status"] in ("Pending", "Accepted")
        ),
        None
    )

    if active:
        st.info(
            f"Request Status: {active['status'].upper()}"
        )

    else:
        student_name = st.text_input(
            "Your name (demo; no login required)",
            value="Demo Student"
        )

        if st.button(
            "📨 Request Tutoring Session",
            type="primary"
        ):
            ok, message = submit(selected, student_name)

            if ok:
                st.success(message)
                st.rerun()
            else:
                st.warning(message)

# Search results
else:
    st.subheader("Available Tutors")

    found = False

    for tutor in slots():
        if (
            (not search or search.lower() in tutor["course"].lower())
            and (date_op is None or date_op == tutor["Date"])
            and (time_op is None or time_op == tutor["time"])
        ):
            found = True

            with st.container(border=True):
                st.subheader(tutor["name"])

                st.write(
                    "Date available:",
                    tutor["Date"].strftime("%m/%d/%Y")
                )

                st.write(
                    "Time available:",
                    tutor["time"].strftime("%I:%M %p")
                )

                st.write("Course:", tutor["course"])
                st.write("Subject:", tutor["subject"])

                active = next(
                    (
                        request for request in requests()
                        if request["slot_id"] == tutor["id"]
                        and request["status"] in ("Pending", "Accepted")
                    ),
                    None
                )

                if active:
                    st.info("Status: " + active["status"])

                if st.button(
                    "View Profile",
                    key="profile_" + tutor["id"]
                ):
                    st.session_state.selected_tutor = tutor["id"]
                    st.rerun()

    if not found:
        st.warning(
            "Sorry! No tutor is available for this time or course."
        )

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

    if st.button(
        "📚 Student Dashboard",
        use_container_width=True
    ):
        st.switch_page("pages/student_dashboard.py")

    if st.button(
        "👩‍🏫 Tutor Dashboard",
        use_container_width=True
    ):
        st.switch_page("pages/tutor_dashboard.py")

