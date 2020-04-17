from typing import *
from datetime import datetime, date, time, timedelta

def solution() -> None:
    h: int
    m: int
    h, m = map(int, input().strip().split())

    origin: date = date(2000, 1, 1)
    target_time: time = time(hour=h, minute=m, second=0)

    alarm_time: time = (datetime.combine(origin, target_time) - timedelta(minutes=45)).time()

    print("{} {}".format(alarm_time.hour, alarm_time.minute))
