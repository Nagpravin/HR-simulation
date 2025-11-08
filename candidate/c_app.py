import streamlit as st
import time
import os
import threading
import cv2
from pymongo import MongoClient
from streamlit_mic_recorder import mic_recorder
from pydub import AudioSegment
from io import BytesIO
from datetime import datetime

# MongoDB Connection
client = MongoClient("mongodb://localhost:27017/")
db = client.hr_recruitment

# Create directories for saving audio & snapshots
os.makedirs("audio", exist_ok=True)
os.makedirs("snapshots", exist_ok=True)

# Initialize session state variables
if "stop_snapshots" not in st.session_state:
    st.session_state["stop_snapshots"] = False
if "recording_started" not in st.session_state:
    st.session_state["recording_started"] = False
if "current_question" not in st.session_state:
    st.session_state["current_question"] = 0

# Function to capture snapshots every 20s
def start_snapshot_capture(user_email, test_id):
    while not st.session_state.get("test_complete", False):
        time.sleep(120)
        capture_snapshot(user_email, test_id)

# Function to capture a snapshot with unique filenames
def capture_snapshot(user_email, test_id):
    cam = cv2.VideoCapture(0)
    ret, frame = cam.read()
    if ret:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")  # Unique timestamp
        filename = f"{user_email}_{test_id}_{timestamp}.jpg"
        filepath = os.path.join("snapshots", filename)
        cv2.imwrite(filepath, frame)
    cam.release()

# Function to save recorded audio
def save_audio(user_email, test_id, question_no, audio_bytes):
    filename = f"{test_id}_{question_no+1}_{user_email}.mp3"
    filepath = os.path.join("audio", filename)

    # Convert recorded audio data to MP3
    audio = AudioSegment.from_file(BytesIO(audio_bytes), format="webm")
    audio.export(filepath, format="mp3")

# Candidate Authentication
def candidate_auth():
    st.title("Candidate Login")
    email = st.text_input("Enter your Email")
    password = st.text_input("Enter your Password", type="password")
    test_id = st.text_input("Enter your Test ID")
    test_password = st.text_input("Enter Test Password", type="password")

    if st.button("Login"):
        user = db.generated_tests.find_one({"test_id": test_id, "test_password": test_password})
        if user:
            st.session_state["candidate_email"] = email
            st.session_state["test_id"] = test_id
            st.session_state["test_data"] = user
            st.success("Login successful! Proceeding to test instructions...")
            st.session_state["auth_done"] = True
            st.rerun()
        else:
            st.error("Invalid credentials. Please check your Test ID and Password.")

# Test Confirmation Page
def candidate_confirmation():
    st.title("Test Confirmation")
    st.write("### Test Instructions:")
    st.write("- The test contains **5 questions**.")
    st.write("- Each question has **30 seconds** of thinking time.")
    st.write("- After 30s, the microphone will **automatically start recording**.")
    st.write("- Click **START** to begin early.")
    st.write("- Click **Go to Next Question** to end recording and move forward.")
    st.write("- Snapshots will be taken automatically every 15 seconds.")

    if st.button("Proceed to Test"):
        st.session_state["test_confirmed"] = True
        st.session_state["current_question"] = 0
        st.session_state["test_complete"] = False
        threading.Thread(target=start_snapshot_capture, args=(st.session_state["candidate_email"], st.session_state["test_id"]), daemon=True).start()
        st.rerun()

# Test Execution Page
def candidate_test():
    st.title("Candidate Test")

    if "test_data" not in st.session_state:
        st.error("Error: No test data found! Please login again.")
        return

    user_email = st.session_state["candidate_email"]
    test_id = st.session_state["test_id"]
    test_data = st.session_state["test_data"]
    questions = test_data["questions"]
    total_questions = len(questions)
    current_question = st.session_state.get("current_question", 0)

    if current_question >= total_questions:  # All questions completed
        st.success("Test Completed! Answers saved.")
        st.session_state["test_complete"] = True
        return

    st.write(f"### Question {current_question + 1}: {questions[current_question]}")

    # Thinking Timer (30s) with Auto-Start Mic
    thinking_placeholder = st.empty()
    if not st.session_state["recording_started"]:
        start_early = st.button("Start Early", key=f"start_early_{current_question}")

        if start_early:
            st.session_state["recording_started"] = True  # Start recording immediately
        else:
            for i in range(30, 0, -1):
                thinking_placeholder.text(f"Thinking Time: {i}s")
                time.sleep(1)
            st.session_state["recording_started"] = True  # Auto-start after 30s

    # Start Recording
    st.write("Recording Started... Speak Now!")
    audio_data = mic_recorder(start_prompt="Recording", stop_prompt="STOP")

    # If last question, show "Submit" instead of "Go to Next Question"
    next_button_label = "Submit" if current_question + 1 == total_questions else f"Go to Question {current_question + 2}"

    # Show "Go to Next Question" Button After Recording Starts
    if st.session_state["recording_started"] and st.button(next_button_label):
        try:
            audio_bytes = audio_data["bytes"]  # Extract audio bytes correctly
            save_audio(user_email, test_id, current_question, audio_bytes)  # Save audio only

            # Reset & Move to Next Question
            st.session_state["recording_started"] = False
            st.session_state["current_question"] += 1
            st.rerun()

        except Exception as e:
            st.error(f"Error saving audio: {e}")

# Run the Candidate Flow
if "auth_done" not in st.session_state:
    candidate_auth()
elif "test_confirmed" not in st.session_state:
    candidate_confirmation()
else:
    candidate_test()
