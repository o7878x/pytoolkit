import time
from typing import Optional, Callable

from src.timer.timer_exception import StartTimerException, EndTimerException, CalculateTimerException


class BaseTimer(object):
    DEFAULT_TIMER_NAME: str = 'BaseTimer'
    DEFAULT_CLOCK_FUNCTION: Callable = time.perf_counter
    DEFAULT_TIME_UNIT: str = 'second'

    def __init__(self, name: str = DEFAULT_TIMER_NAME, *args, **kwargs):
        self._name: str = name or self.DEFAULT_TIMER_NAME
        self._start_time: Optional[float] = None
        self._end_time: Optional[float] = None
        self._elapsed_time: Optional[float] = None

    def reset(self):
        self._start_time, self._end_time, self._elapsed_time = None, None, None

    def start(self):
        if self._start_time:
            raise StartTimerException()
        self._start_time = self.DEFAULT_CLOCK_FUNCTION()

    def end(self):
        if not self._start_time:
            raise EndTimerException()
        self._end_time = self.DEFAULT_CLOCK_FUNCTION()

    def calculate(self) -> float:
        if (not self._start_time) or (not self._end_time):
            raise CalculateTimerException()
        return self._end_time - self._start_time


if __name__ == '__main__':
    timer = BaseTimer()
    timer.start()
    for i in range(1000):
        pass
    timer.end()
    print(timer.calculate())
