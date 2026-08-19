print("jonter7751")

'''Create a program that will act as a calculator.
It should be able to take two values from the keyboard,
accept the operations to be performed and return the computed
average.
'''

THANK_YOU_MESSAGE = '''Thank you for using our calculator'''

WELCOME_MESSAGE = '''Thank you for using our calculator -
You will now be prompted to enter an equation to solve it.
It should be entered on a single line in the format "a+b".
Please be sure you leave at least one space between the operands and
the operators.
We have also added additional functionality to the calculator.
You now have the following operations available:

"+" addition
"-" subtraction
"/" real division
"//" integer division - also called floor division in Python
"%" modulo
"**" take the first operand to the power of the second operand
"!" factorial
'''

from math import factorial


def setup(message):
    print(message)


def getInfo():
    number = input("Please enter your equation: ")

    try:
        if number.count(" ") == 2:
            number1, operation, number2 = number.split(" ")
            number1 = int(number1)
            number2 = int(number2)
        else:
            number1, operation = number.split(" ")
            number1 = int(number1)
            number2 = ""

        return number1, number2, operation

    except:
        return 0, 0, None


def calculate(num1, num2, op):
    if op == '+':
        answer = num1 + num2
    elif op == '-':
        answer = num1 - num2
    elif op == '/':
        answer = num1 / num2
    elif op == "*":
        answer = num1 * num2
    elif op == "//":
        answer = num1 // num2
    elif op == "%":
        answer = num1 % num2
    elif op == "**":
        answer = pow(num1, num2)
    elif op == "!":
        answer = factorial(num1)
    else:
        answer = None

    return answer


def detailLoop(keepGoing):
    while keepGoing == "T":
        number1, number2, operation = getInfo()
        result = calculate(number1, number2, operation)
        displayResult(number1, number2, operation, result)
        keepGoing = input(
            "Do you wish to perform another calculation? (T or F)"
        )


def displayResult(num1, numb, op, answer):
    print(f"The answer to {num1} {op} {numb} == {answer}")


def finishUp(message):
    print(message)


def main():
    keepGoing = "T"
    setup(WELCOME_MESSAGE)
    detailLoop(keepGoing)
    finishUp(THANK_YOU_MESSAGE)


main()
