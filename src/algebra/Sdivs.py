# Source/algerbra/Sdivs.py
# Calculating the sum of divisators of a given number


def sum_div(x):
    s = 0

    for i in range(1, x // 2 + 1):
        if x % i == 0:
            s += i
    return s
