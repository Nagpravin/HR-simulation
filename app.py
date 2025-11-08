import streamlit as st
import auth
import questions
import evaluation
import test_generator

if "hr_logged_in" not in st.session_state:
    auth.login_page()
elif "test_data" not in st.session_state:
    questions.question_selection_page()
elif "evaluation_criteria" not in st.session_state:
    evaluation.evaluation_criteria_page()
else:
    test_generator.generate_test_ids_page()