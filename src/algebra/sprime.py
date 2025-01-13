# Source/algerbra/sprime.py
# Checking if the number is semi-prime
from algebra.prime import prime

def sprime(x):
    factors = []
    for i in range(2, x + 1):
        if x % i == 0 and prime(i):
            factors.append(i)
            if len(factors) > 2:
                return False
    return len(factors) == 2