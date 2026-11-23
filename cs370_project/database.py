import psycopg2
import streamlit as st

def get_connection():
    return psycopg2.connect(
        st.secrets["postgres"]["url"],
        sslmode="require",
        connect_timeout=10
    )


