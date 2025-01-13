# Source/algerbra/factoriel.py
# Calculating the factorial of a given number
from rich import print

def factorial(x:int):
    results:int = 1
    if x == 0:
        results = 1
    elif x == 1:
        results = 1
    else:
        for i in range(1, x+1):
            results *= i
            print(f'restults:{results} and i: {i}')
    return results