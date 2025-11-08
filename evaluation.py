import streamlit as st
from pymongo import MongoClient
import pandas as pd
import random
import string 

# MongoDB Connection
client = MongoClient("mongodb://localhost:27017/")
db = client.hr_recruitment
generated_tests_collection = db.generated_tests  
evaluation_criteria_collection = db.evaluation_criteria  

def generate_test_id():
    """Generates a random test ID and password"""
    test_id = "TEST-" + "".join(random.choices(string.ascii_uppercase + string.digits, k=6))
    test_password = "".join(random.choices(string.ascii_letters + string.digits, k=8))
    return test_id, test_password 

def evaluation_criteria_page():
    st.title("Select Evaluation Criteria")

    # Fetch evaluation criteria from MongoDB
    criteria_list = [c["name"] for c in evaluation_criteria_collection.find()]
    
    # Display evaluation criteria in tabular format with checkboxes
    st.write("### Select Evaluation Criteria")
    criteria_dict = {c: st.checkbox(c, key=f"crit_{c}") for c in criteria_list}
    selected_criteria = [c for c, checked in criteria_dict.items() if checked]

    if st.button("Submit Evaluation Criteria"):
        if "test_data" not in st.session_state:
            st.error("Error: No test data found! Please go back and select questions first.")
            return

        test_id, test_password = generate_test_id()

        # Store everything in `generated_tests`
        test_data = {
            "email": st.session_state["test_data"]["email"],
            "questions": st.session_state["test_data"]["questions"],
            "predefined_answers": st.session_state["test_data"]["predefined_answers"],
            "keywords": st.session_state["test_data"]["keywords"],
            "evaluation_criteria": selected_criteria,
            "test_id": test_id,
            "test_password": test_password
        }
        generated_tests_collection.insert_one(test_data)

        st.success(f"Evaluation Criteria Submitted Successfully!")
        st.write(f"**Test ID:** {test_id}")
        st.write(f"**Test Password:** {test_password}")

        st.session_state["test_credentials"] = {"test_id": test_id, "test_password": test_password}

        if st.button("Close Application"):
            import os
            os.system("taskkill /IM python.exe /F")

# import streamlit as st
# import random
# import string
# import os
# import sys
# from pymongo import MongoClient

# client = MongoClient("mongodb://localhost:27017/")
# db = client.hr_recruitment
# tests_collection = db.generated_tests

# def generate_password(length=8):
#     return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

# def evaluation_criteria_page():
#     st.title("Select Evaluation Criteria")
#     criteria_collection = db.evaluation_criteria
#     criteria = list(criteria_collection.find())
#     selected_criteria = []
    
#     for criterion in criteria:
#         if st.checkbox(criterion["name"], key=criterion["name"]):
#             selected_criteria.append(criterion["name"])
    
#     if st.button("Save Evaluation Criteria"):
#         if "test_data" in st.session_state:
#             st.session_state["test_data"]["evaluation_criteria"] = selected_criteria
#             st.success("Evaluation criteria saved successfully!")
            
#             # Generate Test ID and Password
#             test_id = f"Test-{random.randint(1000, 9999)}"
#             test_password = generate_password()
#             st.session_state["test_data"]["test_id"] = test_id
#             st.session_state["test_data"]["test_password"] = test_password
            
#             # Store in MongoDB
#             tests_collection.insert_one(st.session_state["test_data"])
            
#             st.success(f"Test ID: {test_id}, Password: {test_password} (Share with candidates)")
            
#             # Button to close application and shutdown browser
#             if st.button("Close Application"):
#                 st.write("Closing application...")
#                 os.system("taskkill /IM python.exe /F")  # Force close the app
#                 sys.exit()
#         else:
#             st.error("Please select questions first!")