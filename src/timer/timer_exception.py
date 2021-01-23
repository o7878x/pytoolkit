class BaseTimerException(RuntimeError):
    def __init__(self, msg: str):
        self.msg = msg


class StartTimerException(BaseTimerException):
    DEFAULT_MSG: str = 'already start timer and please invoke end().'

    def __init__(self, msg: str = DEFAULT_MSG):
        tmp_msg: str = msg or self.DEFAULT_MSG
        super().__init__(tmp_msg)


class EndTimerException(BaseTimerException):
    DEFAULT_MSG: str = 'already end timer and please invoke start().'

    def __init__(self, msg: str = DEFAULT_MSG):
        tmp_msg: str = msg or self.DEFAULT_MSG
        super().__init__(tmp_msg)


class CalculateTimerException(BaseTimerException):
    DEFAULT_MSG: str = 'never start and end timer.'

    def __init__(self, msg: str = DEFAULT_MSG):
        tmp_msg: str = msg or self.DEFAULT_MSG
        super().__init__(tmp_msg)


if __name__ == '__main__':
    print(StartTimerException().msg)
    print(EndTimerException().msg)
    print(CalculateTimerException().msg)
