#!/usr/bin/env python
from __future__ import print_function

# from datetime import datetime
import time
from typing import Dict, Optional

"""
Simple Timer class module, used to allow either simple elapsed time using
with clause, or by using named timers with the start, get and reset methods 
"""


class TimerNotFoundException(Exception):
    """Exception thrown if timer not in dictionary"""

    pass


class Timer:
    """Simple elapsed timer class can be used in a with clause or as stand alone named timers."""

    timers = dict()
    """this is a class attribute used by the class methods"""

    def __init__(self):
        """Init method does nothing."""
        pass

    def __enter__(self):
        """Start a timer if using with statement."""
        self.start = time.time_ns()

    def __exit__(self, type, value, traceback):
        """End timer and report if using with statement."""
        end = time.time_ns()
        delta = end - self.start
        print("Elapsed time {} ms".format(delta / 1e6))
        return False

    @classmethod
    def add_timer(cls, name: str):
        """Add timer to the class timer dictionary"""
        Timer.timers[name] = None

    @classmethod
    def start_timer(cls, name: str):
        """Start / reset the named timer or throw exception."""
        if Timer.timers.get(name) is None:
            Timer.timers[name] = time.time_ns()
        else:
            raise TimerNotFoundException

    @classmethod
    def remove_timer(cls, name: str):
        """Remove the named timer or throw exception."""
        if Timer.timers.get(name) is not None:
            del Timer.timers[name]
        else:
            raise TimerNotFoundException

    @classmethod
    def get_elapsed_ms(cls, name: str) -> float:
        """Get elapsed time as ms for named timer"""
        if Timer.timers.get(name) is not None:
            end = time.time_ns()
            delta = end - Timer.timers[name]
            return delta / 1e6

        else:
            raise TimerNotFoundException

    @classmethod
    def get_elapsed_ns(cls, name: str) -> float:
        """Get elapsed time as nano seconds for named timer"""
        if Timer.timers.get(name) is not None:
            end = time.time_ns()
            delta = end - Timer.timers[name]
            return delta
        else:
            raise TimerNotFoundException

    @classmethod
    def get_elapsed_s(cls, name: str) -> float:
        """Get elapsed time as seconds for named timer"""
        if Timer.timers.get(name) is not None:
            end = time.time_ns()
            delta = end - Timer.timers[name]
            return delta / 1e9
        else:
            raise TimerNotFoundException


if __name__ == "__main__":
    print("Running Timer Tests")
    print("using with statement")
    with Timer() as t:
        time.sleep(1)
    print("Test adding named timer")
    Timer.add_timer("TestTimer")
    Timer.start_timer("TestTimer")
    for i in range(0, 5):
        time.sleep(1)
        print("Getting elapsed {} ms".format(Timer.get_elapsed_ms("TestTimer")))
        print("Getting elapsed {} ns".format(Timer.get_elapsed_ns("TestTimer")))
        print("Getting elapsed {} s".format(Timer.get_elapsed_s("TestTimer")))
    print("test remove timer and call")
    Timer.remove_timer("TestTimer")
    try:
        Timer.get_elapsed_ms("TestTimer")
    except TimerNotFoundException:
        print("Named timer doesn't exist")
    print("end of tests")
