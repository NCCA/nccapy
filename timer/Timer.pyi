from typing import Any

class TimerNotFoundException(Exception): ...

class Timer:
    timers: Any
    def __init__(self) -> None: ...
    start: Any
    def __enter__(self) -> None: ...
    def __exit__(self, type, value, traceback): ...
    @classmethod
    def add_timer(cls, name: str): ...
    @classmethod
    def start_timer(cls, name: str): ...
    @classmethod
    def remove_timer(cls, name: str): ...
    @classmethod
    def get_elapsed_ms(cls, name: str) -> float: ...
    @classmethod
    def get_elapsed_ns(cls, name: str) -> float: ...
    @classmethod
    def get_elapsed_s(cls, name: str) -> float: ...