class CustomException(Exception):
    def __init__(self, message: str):
        super().__init__(self)
        self.message: str = message

    def __str__(self):
        return self.message
