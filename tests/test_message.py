from message import Message

test_content = "test content"
test_role = "user"


def test_create_message_success():
    message = Message(test_content)
    assert message.content == test_content
    assert message.role == test_role


def test_convert_to_dict_success():
    message = Message(test_content)
    message_dict = message.to_dict()
    assert message_dict["content"] == test_content
    assert message_dict["role"] == test_role
