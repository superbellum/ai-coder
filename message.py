class Message:
    def __init__(self, content: str, role: str = "user"):
        self.content = content
        self.role = role

    def to_dict(self):
        return dict(content=self.content, role=self.role)
