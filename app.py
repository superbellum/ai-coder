import streamlit as st

from message import Message
from model import OpenaiModel

model = OpenaiModel()

st.title("AI-coder app")


def get_answer_from_model(question_text: str) -> str:
    return model.get_answer(question=Message(question_text))


def send_question():
    question_text = st.session_state.question_input
    st.session_state.question_input = ""

    if question_text:
        st.session_state.answer_output = get_answer_from_model(question_text)


question_input = st.text_input("Please, enter your question:", key="question_input")

st.button("Send", on_click=send_question)

if "answer_output" in st.session_state:
    st.write(st.session_state.answer_output)
