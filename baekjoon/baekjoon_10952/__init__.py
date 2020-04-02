def solution():
    a: int
    b: int

    a, b = map(int, input().strip().split(" "))

    if a != 0 and b != 0:
        print(a + b)
        solution()
