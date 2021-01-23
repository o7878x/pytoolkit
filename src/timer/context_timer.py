from src.timer.base_timer import BaseTimer


class ContextTimer(BaseTimer):
    DEFAULT_TIMER_NAME = 'ContextTimer'

    def __init__(self, name=DEFAULT_TIMER_NAME, *args, **kwargs):
        super().__init__(name, args, kwargs)

    def __enter__(self):
        self.start()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end()
        print(f'elapsed time{self._name} : {self.calculate()} {self.DEFAULT_TIME_UNIT}s')


if __name__ == '__main__':
    with ContextTimer() as timer:
        for i in range(10000):
            pass
