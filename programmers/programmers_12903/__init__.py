def solution(s: str) -> str:
    mid: int = len(s) // 2
    return s[mid] if len(s) % 2 > 0 else s[mid-1:mid+1]
