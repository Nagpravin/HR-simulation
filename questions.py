import streamlit as st
from pymongo import MongoClient
import pandas as pd
import random
import string

# MongoDB Connection
client = MongoClient("mongodb://localhost:27017/")
db = client.hr_recruitment
questions3_collection = db.questions3_collection  
generated_tests_collection = db.generated_tests  

def question_selection_page():
    st.title("Select Questions for the Test")

    # Fetch all questions from MongoDB
    questions = list(questions3_collection.find({}, {"question": 1, "answers": 1, "keywords": 1, "_id": 0}))

    selected_questions = []
    predefined_answers = {}
    selected_keywords = {}

    for i in range(5):
        st.write(f"### Question {i+1}")

        # Checkbox for custom question
        use_custom_question = st.checkbox(f"Use Custom Question for Question {i+1}", key=f"custom_q{i}")

        if use_custom_question:
            question_text = st.text_input(f"Enter Custom Question {i+1}", key=f"custom_question_{i}")
            predefined_answers[question_text] = [
                st.text_area(f"Predefined Answer 1", key=f"a1_{i}"),
                st.text_area(f"Predefined Answer 2", key=f"a2_{i}"),
                st.text_area(f"Predefined Answer 3", key=f"a3_{i}")
            ]
            selected_keywords[question_text] = st.text_area(
                f"Enter Keywords for Question {i+1} (Separate by commas)", key=f"k{i}"
            ).split(",")
        else:
            question_text = st.selectbox(
                f"Select Question {i+1}",
                [q["question"] for q in questions],
                key=f"q{i}"
            )
            question_data = next(q for q in questions if q["question"] == question_text)
            predefined_answers[question_text] = [
                st.text_area(f"Predefined Answer 1", question_data["answers"][0], key=f"a1_{i}"),
                st.text_area(f"Predefined Answer 2", question_data["answers"][1], key=f"a2_{i}"),
                st.text_area(f"Predefined Answer 3", question_data["answers"][2], key=f"a3_{i}")
            ]
            # Now using text area instead of dropdown for keywords
            selected_keywords[question_text] = st.text_area(
                f"Enter Keywords for Question {i+1} (Separate by commas)",
                ", ".join(question_data.get("keywords", [])),  # Prefill with existing keywords
                key=f"k{i}"
            ).split(",")

        selected_questions.append(question_text)

    if st.button("Review & Submit Questions"):
        st.session_state["test_data"] = {
            "email": st.session_state.get("hr_email", "unknown"),
            "questions": selected_questions,
            "predefined_answers": predefined_answers,
            "keywords": selected_keywords
        }
        st.success("Questions saved successfully! Proceeding to review page...")
        st.rerun()

    if "test_data" in st.session_state:
        st.title("Review Selected Questions")

        review_data = []
        for idx, question in enumerate(st.session_state["test_data"]["questions"]):
            review_data.append([
                f"Q{idx+1}",
                question,
                " | ".join(st.session_state["test_data"]["predefined_answers"][question]),
                ", ".join(st.session_state["test_data"]["keywords"][question])
            ])

        review_df = pd.DataFrame(review_data, columns=["#", "Question", "Predefined Answers", "Keywords"])
        st.table(review_df.style.set_properties(**{"border": "1px solid black", "padding": "5px"}))

        if st.button("Confirm & Proceed to Evaluation Criteria"):
            st.success("Proceeding to Evaluation Criteria Page...")
            st.switch_page("evaluation.py")

# import streamlit as st
# from pymongo import MongoClient
# import pandas as pd

# # MongoDB Connection
# client = MongoClient("mongodb://localhost:27017/")
# db = client.hr_recruitment
# questions_collection = db.questions
# test_collection = db.generated_tests  # Collection to store selected questions

# def question_selection_page():
#     st.title("Select Questions for the Test")

#     # Fetch all questions from MongoDB
#     questions = list(questions_collection.find())

#     # Fetch all unique keywords from the database
#     all_keywords = list(set(keyword for q in questions for keyword in q["keywords"]))

#     selected_questions = []
#     predefined_answers = {}
#     selected_keywords = {}

#     for i in range(5):
#         st.write(f"### Question {i+1}")

#         # Option to choose between selecting a question or adding a custom one
#         use_custom_question = st.checkbox(f"Use Custom Question for Question {i+1}", key=f"custom_q{i}")

#         if use_custom_question:
#             question_text = st.text_input(f"Enter Custom Question {i+1}", key=f"custom_question_{i}")
#             predefined_answer = st.text_area(f"Predefined Answer for Custom Question {i+1}", key=f"custom_answer_{i}")
#         else:
#             question_text = st.selectbox(
#                 f"Select Question {i+1}",
#                 [q["question"] for q in questions],
#                 key=f"q{i}"
#             )

#             # Fetch predefined answer automatically
#             predefined_answer = next((q["answers"][0] for q in questions if q["question"] == question_text), "")
#             predefined_answer = st.text_area(
#                 f"Predefined Answer for Question {i+1}",
#                 predefined_answer,
#                 key=f"a{i}"
#             )

#         predefined_answers[question_text] = predefined_answer
#         selected_questions.append(question_text)

#         # Allow HR to select multiple keywords from the full keyword list
#         selected_keywords[question_text] = st.multiselect(
#             f"Select Keywords for Question {i+1}",
#             all_keywords,  # Showing all keywords
#             key=f"k{i}"
#         )

#         # Display available keywords in a table format
#         # df = pd.DataFrame({"Available Keywords": all_keywords})
#         # st.table(df.style.set_properties(**{"text-align": "center", "border": "1px solid black", "padding": "5px"}))

#     if st.button("Save Questions"):
#         test_data = {
#             "email": st.session_state.get("hr_email", "unknown"),  # Get HR email from session
#             "questions": selected_questions,
#             "predefined_answers": predefined_answers,
#             "keywords": selected_keywords  # Stores selected keywords for each question
#         }

#         # Store in MongoDB
#         test_collection.insert_one(test_data)

#         st.success("Questions and keywords saved successfully!")
#         st.rerun()
