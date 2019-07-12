class ChemException(BaseException):
    def __init__(self, msg: str = ""):
        self.message = msg


class ParseError(ChemException):
    def __init__(self, msg: str = "", data: str = ""):
        super().__init__(msg)
        self.data = data
