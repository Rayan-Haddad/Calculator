# Source/algerbra/calculation.py
# The calulating algorithms
import logging
import sys

sys.path.append("../")
from rich import print
from utilities.InputUtils import CleanInput
from utilities.InputUtils import replaceElement
from utilities.InputUtils import ConcatinateNumbers
from factorial import factorial

logging.basicConfig(
    level=logging.DEBUG,
    format="[%(asctime)s] [%(levelname)s]: \n%(message)s",
    datefmt="%Y/%m/%d{%H:%M:%S}",
)


# Calculate Multiplication:
def multiplication(Equation: list):
    print("Multi")
    i = 0
    while i < len(Equation):
        if i < len(Equation) and Equation[i] == "*":
            result = float(Equation[i - 1]) * float(Equation[i + 1])
            print(result)
            Equation[i] = "?"
            print(Equation)
            Equation.pop(i + 1)
            Equation.pop(i - 1)
            print(Equation)
            replaceElement(Equation, "?", result)
        else:
            i += 1
    print(Equation)


def division(Equation: list):
    print("division")
    i = 0
    while i < len(Equation):
        if i < len(Equation) and Equation[i] == "/":
            result = float(Equation[i - 1]) / float(Equation[i + 1])
            print(result)
            Equation[i] = "?"
            print(Equation)
            Equation.pop(i + 1)
            Equation.pop(i - 1)
            print(Equation)
            replaceElement(Equation, "?", result)
        else:
            i += 1
    print(Equation)


def Addition(Equation: list):
    print("Starting addition")
    i = 0
    while i < len(Equation):
        if i < len(Equation) and Equation[i] == "+":
            print("Addition first statement")
            result = float(Equation[i - 1]) + float(Equation[i + 1])
            print(result)
            Equation[i] = "?"
            print(Equation)
            Equation.pop(i + 1)
            Equation.pop(i - 1)
            replaceElement(Equation, "?", result)
            print("Equation:", Equation)
        elif i < len(Equation) and Equation[i] == "-":
            print("Addition second statement")
            result = float(Equation[i - 1]) - float(Equation[i + 1])
            Equation[i] = "?"
            print(result)
            Equation.pop(i + 1)
            Equation.pop(i - 1)
            print(Equation)
            replaceElement(Equation, "?", result)
            print(Equation)
        else:
            i += 1


def lastfound(x: list, target: str):
    s: int = 0
    for i in range(len(x)):
        if x[i] == target:
            s = i
            break
    return s


def count(x: list, target: str):
    s: int = 0
    for i in range(len(x)):
        if x[i] == target:
            s += 1
    return s


def Listfind(x: list, target: str):
    s: int = 0
    for i in range(len(x)):
        if x[i] == target:
            s = i
            break
    return s


def has(x: list, target: list):
    l = False
    for i in range(len(x)):
        if x[i] in target:
            l = True
            break
    return l


# TODO this func
def realizeBrackets(Equation: list):
    openBrackets: list[str] = ["(", "["]
    closedBrackets: list[str] = [")", "]"]
    if count(Equation, "(") != count(Equation, ")") or count(
        Equation, "["
    ) != count(Equation, "]"):
        print("Error in the brackets")
    else:
        l: list = Equation
        eq: list = l[
            lastfound(l, openBrackets[0]) : lastfound(l, closedBrackets[0])
        ]
        if has(eq, openBrackets) or has(eq, closedBrackets):
            realizeBrackets(eq)
        else:
            l[
                lastfound(l, openBrackets[0]) : lastfound(l, closedBrackets[0])
            ] = calculation(eq)
            realizeBrackets(eq)


def realizePower(Equation: list):
    print("Power")
    i = 0
    while i < len(Equation):
        if i < len(Equation) and Equation[i] == "^":
            result = float(Equation[i - 1]) ** float(Equation[i + 1])
            print(result)
            Equation[i] = "?"
            print(Equation)
            Equation.pop(i + 1)
            Equation.pop(i - 1)
            print(Equation)
            replaceElement(Equation, "?", result)
        else:
            i += 1
    print(Equation)


def realizeFactorial(Equation: list):
    print("Factorial")
    i = 0
    while i < len(Equation):
        if (
            i < len(Equation) - 1
            and Equation[i] not in ["/", "*", "+", "-"]
            and Equation[i + 1] == "!"
        ):
            result = factorial(int(Equation[i]))
            print(result)
            Equation[i] = result
            print(Equation)
            Equation.pop(i + 1)
            print(Equation)

        else:
            i += 1
    print(Equation)


def realizeRoots(Equation: list): ...


# calculate
def calculation(Equation):
    eq: list = CleanInput(Equation)
    print(eq)
    ConcatinateNumbers(eq)
    MainList: list = eq
    print("=============")
    print(MainList)
    print("=================")
    print(eq, "recieved list")
    openBrackets: list[str] = ["(", "["]
    closedBrackets: list[str] = [")", "]"]
    if has(eq, openBrackets) or has(eq, closedBrackets):
        realizeBrackets(eq)
    realizeFactorial(MainList)
    realizePower(MainList)
    multiplication(MainList)
    division(MainList)
    Addition(MainList)
    return eq


x = input("Enter something: ")
calculation(x)
