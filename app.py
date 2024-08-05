import streamlit as st

st.title("AI-coder app")


def send_question():
    question_text = st.session_state.question_input
    st.session_state.answer_output = "answer from ai model"


question_input = st.text_input("Please, enter your question:", key="question_input")

st.button("Send", on_click=send_question)

if "answer_output" in st.session_state:
    st.text("The answer from AI model:")
    st.write(st.session_state.answer_output)
