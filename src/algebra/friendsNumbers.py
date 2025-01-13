# Source/algerbra/friendsNumbers.py
# Checking if the numbers are both friends

from algebra.Sdivs import sum_div

def friends(x, y):
    if sum_div(x) == y and sum_div(y) == x:
        return True
    else:
        return False