import streamlit as st
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client.hr_recruitment
user_collection = db.user_accounts
tests_collection = db.generated_tests

def candidate_login_page():
    st.title("Candidate Login")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    test_id = st.text_input("Test ID")
    test_password = st.text_input("Test Password", type="password")
    
    if st.button("Login"):
        user = user_collection.find_one({"email": email, "password": password})
        test = tests_collection.find_one({"test_id": test_id, "test_password": test_password})
        
        if user and test:
            st.session_state["candidate_logged_in"] = True
            st.session_state["candidate_email"] = email
            st.session_state["test_id"] = test_id
            st.success("Login Successful!")
            st.rerun()
        else:
            st.error("Invalid Credentials or Test Details")