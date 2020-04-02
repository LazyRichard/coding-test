def solution():
    a: int
    b: int

    try:
        a, b = map(int, input().strip().split(" "))
    except:
        return
    else:
        print(a + b)
        solution()
