from rich import print

def perfect(x: int):
    s: int = 0
    for i in range(1, x//2+1):
        if x % i == 0:
            s += i
    return s == x