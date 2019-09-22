class ValidationResult:
    def __init__(self):
        self.__status = "OK"
        self.__message = ""

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, status: str):
        self.__status = status

    @property
    def message(self):
        return self.__message

    @message.setter
    def message(self, message: str):
        self.__message = message