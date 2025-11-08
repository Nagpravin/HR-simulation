import streamlit as st
import time
import cv2
import os
from pymongo import MongoClient
import numpy as np

# MongoDB Connection
client = MongoClient("mongodb://localhost:27017/")
db = client.hr_recruitment
candidate_answers_collection = db.candidate_answers  # Stores audio responses
user_snapshots_collection = db.user_snapshots  # Stores snapshots

# Function to capture a snapshot
def capture_snapshot(user_email, question_number):
    cam = cv2.VideoCapture(0)  # Open camera
    ret, frame = cam.read()
    if ret:
        filename = f"snapshot_{user_email}_q{question_number}_{int(time.time())}.jpg"
        filepath = os.path.join("snapshots", filename)
        cv2.imwrite(filepath, frame)  # Save snapshot
        # Store in MongoDB
        user_snapshots_collection.update_one(
            {"email": user_email},
            {"$push": {"snapshots": filepath}},  # Append new snapshot filename
            upsert=True  # Create entry if not exists
        )
    cam.release()

def candidate_test_page():
    st.title("Candidate Test")
    
    # Request Camera & Mic Permissions
    st.write("Please **allow camera and microphone permissions** to proceed.")
    
    if st.button("Grant Permissions & Start Test"):
        st.session_state["permissions_granted"] = True
        st.rerun()

    if not st.session_state.get("permissions_granted"):
        return

    # Get user test details
    user_email = st.text_input("Enter your Email ID")
    test_id = st.text_input("Enter your Test ID")

    if not user_email or not test_id:
        st.warning("Please enter your Email and Test ID to start.")
        return

    # Fetch test details from MongoDB
    test_data = db.generated_tests.find_one({"test_id": test_id})
    if not test_data:
        st.error("Invalid Test ID. Please check and try again.")
        return

    questions = test_data["questions"]  # List of 5 questions
    answers = {}

    # Create a folder for snapshots
    os.makedirs("snapshots", exist_ok=True)

    for idx, question in enumerate(questions):
        st.write(f"### Question {idx+1}: {question}")

        # Thinking Time (30s) with Option to Start Early
        start_early = st.button("Start Answer Early", key=f"start_early_{idx}")
        if not start_early:
            with st.empty():
                for i in range(30, 0, -1):
                    st.write(f"Thinking Time: {i}s")
                    time.sleep(1)

        # Answer Recording (Max 2m 30s)
        st.write("Recording Started... Speak Now!")
        st.session_state[f"recording_{idx}"] = True
        start_time = time.time()
        stop_early = st.button("Stop Recording", key=f"stop_{idx}")

        while time.time() - start_time < 150:  # 150 seconds (2m 30s)
            elapsed = int(time.time() - start_time)
            st.write(f"Recording Time: {elapsed}s / 150s")

            # Capture snapshot every 20s
            if elapsed % 20 == 0 and elapsed > 0:
                capture_snapshot(user_email, idx + 1)

            if stop_early:
                st.write("Recording Stopped.")
                break

            time.sleep(1)

        st.write("Recording Complete.")

        # Store audio path (Placeholder, actual audio saving needs implementation)
        answers[question] = f"audio_response_q{idx+1}.wav"

    # Store Responses in MongoDB
    candidate_response = {
        "email": user_email,
        "test_id": test_id,
        "questions": questions,
        "answers": answers
    }
    candidate_answers_collection.insert_one(candidate_response)

    st.success("Test Completed! Your responses have been saved.")
