from openai import OpenAI

from message import Message


class OpenaiModel:
    def __init__(self):
        self.client = OpenAI()

    def get_answer(self, question: Message):
        return self.client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[question.to_dict()],
            max_tokens=150
        ).choices[0].message.content
