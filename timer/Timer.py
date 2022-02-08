#!/usr/bin/env python
from __future__ import print_function
from datetime import datetime


class Timer:
    """
    Simple elapsed timer class can be used in a with clause or as stand alone named timers
    """

    def __init__(self):
        pass

    def __enter__(self):
        self.start = datetime.now()

    def __exit__(self, type, value, traceback):
        end = datetime.now()
        delta = end - self.start
        print("Elapsed time {} ms".format(int(delta.total_seconds() * 1000)))
        return False


if __name__ == "__main__":
    import time

    print("Running Timer Test")
    with Timer() as t:
        time.sleep(1)
