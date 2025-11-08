import streamlit as st
from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client.hr_recruitment
hr_collection = db.hr_users

def login_page():
    st.title("HR Login")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    
    if st.button("Login"):
        hr = hr_collection.find_one({"email": email, "password": password})
        if hr:
            st.session_state["hr_logged_in"] = True
            st.session_state["hr_email"] = email
            st.success("Login Successful!")
            st.rerun()
        else:
            st.error("Invalid Credentials")