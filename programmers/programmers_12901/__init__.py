from datetime import date

def solution(mon: int, day: int) -> str:
    return date(2016, mon, day).strftime("%a").upper()
