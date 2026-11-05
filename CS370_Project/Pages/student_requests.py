
import streamlit as st
from session_store import requests, decide
st.set_page_config(
    page_title="TutorHub",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)
st.title("📩 Student Requests")

st.write(
    "Review tutoring requests from students "
    "and accept or decline them."
)

st.divider()

all_requests = requests()

if not all_requests:
    st.info("No student requests yet.")

for item in all_requests:

    with st.container(border=True):

        st.write("Student:", item["student"])
        st.write("Tutor:", item["tutor"])
        st.write("Course:", item["course"])

        st.write(
            "Requested Time:",
            item["when"].strftime("%m/%d/%Y %I:%M %p")
        )

        st.write("Status:", item["status"])

        if item["status"] == "Pending":

            col1, col2 = st.columns(2)

            with col1:
                if st.button(
                    "Accept",
                    key=f"accept_{item['id']}",
                    use_container_width=True,
                    type="primary"
                ):
                    decide(item["id"], "Accepted")
                    st.rerun()

            with col2:
                if st.button(
                    "Decline",
                    key=f"decline_{item['id']}",
                    use_container_width=True
                ):
                    decide(item["id"], "Declined")
                    st.rerun()

        elif item["status"] == "Accepted":
            st.success("Request Accepted")

        elif item["status"] == "Declined":
            st.error("Request Declined")

st.divider()

if st.button("⬅ Back to Tutor Dashboard"):
    st.switch_page("pages/tutor_dashboard.py")

# Sidebar navigation
with st.sidebar:

    st.title("🎓 TutorHub")
    st.divider()

    if st.button("🏠 Home", use_container_width=True):
        st.switch_page("app.py")


