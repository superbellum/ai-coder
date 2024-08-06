import pytest
from unittest.mock import MagicMock, patch
from model import OpenaiModel
from message import Message

test_answer = "test answer"
test_question_dict = {"role": "user", "content": "test question"}


@patch('model.OpenAI')
def test_get_answer(mock_openai):
    model = OpenaiModel()

    mock_message = MagicMock(spec=Message)
    mock_message.to_dict.return_value = test_question_dict

    mock_response = MagicMock()
    mock_response.choices = [MagicMock(message=MagicMock(content=test_answer))]
    model.client.chat.completions.create.return_value = mock_response

    answer = model.get_answer(mock_message)

    assert answer == test_answer
    model.client.chat.completions.create.assert_called_once_with(
        model="gpt-4o-mini",
        messages=[test_question_dict],
        max_tokens=150
    )
