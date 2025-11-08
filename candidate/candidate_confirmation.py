# import streamlit as st

# def candidate_confirmation_page():
#     st.title("Test Confirmation")

#     st.write("### Test Instructions:")
#     st.write("- The test contains **5 questions**.")
#     st.write("- Each question has **30 seconds** of thinking time.")
#     st.write("- You will have **2 minutes 30 seconds** to record your answer.")
#     st.write("- Snapshots will be taken automatically during the test.")
#     st.write("- Click on the **mic button** to start recording your answer.")

#     if st.button("Proceed to Test"):
#         st.session_state["test_confirmed"] = True
#         st.switch_page("candidate_test.py")  # Redirects to test-taking page
import streamlit as st

def candidate_confirmation_page():
    st.title("Test Confirmation")

    st.write("### Test Instructions:")
    st.write("- The test contains **5 questions**.")
    st.write("- Each question has **30 seconds** of thinking time.")
    st.write("- You will have **2 minutes 30 seconds** to record your answer.")
    st.write("- Snapshots will be taken automatically during the test.")
    st.write("- Click on the **mic button** to start recording your answer.")

    if st.button("Proceed to Test"):
        st.session_state["test_confirmed"] = True
        st.switch_page("pages/candidate_test.py")  # Correct relative path
