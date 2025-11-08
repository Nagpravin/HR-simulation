import streamlit as st
import random
import string
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client.hr_recruitment
tests_collection = db.generated_tests

def generate_password(length=8):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def generate_test_ids_page():
    st.title("Generate Test Credentials")
    count = st.number_input("Enter the number of candidates", min_value=1, step=1)
    
    if st.button("Generate"):
        test_ids = [{"id": f"Test-{i+1}", "password": generate_password()} for i in range(count)]
        if "test_data" in st.session_state:
            st.session_state["test_data"]["test_ids"] = test_ids
            tests_collection.insert_one(st.session_state["test_data"])  # Save to MongoDB
            st.success("Test credentials generated successfully!")
            st.json(test_ids)
        else:
            st.error("Please select questions and evaluation criteria first!")