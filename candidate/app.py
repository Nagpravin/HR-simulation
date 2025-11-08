import streamlit as st
import candidate_auth
import candidate_confirmation

if "candidate_logged_in" not in st.session_state:
    candidate_auth.candidate_login_page()
elif "test_confirmed" not in st.session_state:
    candidate_confirmation.candidate_confirmation_page()