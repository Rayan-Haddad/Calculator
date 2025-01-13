from rich import print

def pgcd(x:int, y:int):
    while x!=y:
        if x>y:
            x-=y
        else:
            y-=x
    return x