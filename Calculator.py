from math import *

print("Hello! welcome to simple calculator...")


def options():
    print("------------------------------------------------------------------")
    print("choices: ")
    print("Enter '+' to add two numbers")
    print("Enter '-' to subtract two numbers")
    print("Enter '*' to multiply two numbers")
    print("Enter '/' to divide two numbers")
    print("Enter '**' to power two numbers")
    print("Enter '&' to square root ")
    print("Enter 'exit' to exit the calculator")
    print("------------------------------------------------------------------")


# divide function


def divide():
    num1, num2 = float(input("Enter first number: ")), float(input("Enter second number: "))
    if num2 == 0:
        print("Error: division by zero is not possible!")
    else:
        result = num1 / num2
        print("The answer: ", result, "\n")
    x = input("do you want continue? (y/n) ")
    if x == "y" or x == "Y":
        divide()
    elif x == "n" or x == "N":
        print("Good bye!\n------------------------------------------------------------------")
    else:
        exit


# Add function
def add():
    try:
        num1, num2 = float(input("Enter first number: ")), float(input("Enter second number: "))
        result = num1 + num2
        print("The answer: ", result, "\n")
    except:
        print("An error occurred!")
    r = input("do you want continue? (y/n) ")
    if r == "y" or r == "Y":
        add()
    elif r == "n" or r == "N":
        print("Good bye!\n------------------------------------------------------------------")
    else:
        exit


# Subtract function
def subtract():
    try:
        num1, num2 = float(input("Enter first number: ")), float(input("Enter second number: "))
        result = num1 - num2
        print("The answer: ", result, "\n")
    except:
        print("An error occurred!")
    finally:
        z = input("do you want continue? (y/n) ")
        if z == "y" or z == "Y":
            subtract()
        elif z == "n" or z == "N":
            print("Good bye!\n------------------------------------------------------------------")
        else:
            exit


# Multiply function
def multiply():
    try:
        num1, num2 = float(input("Enter first number: ")), float(input("Enter second number: "))
        result = num1 * num2
        print("The answer: ", result, "\n")
    except:
        print("An error ooccured!")
    finally:
        y = input("do you want continue? (y/n) ")
        if y == "y" or y == "Y":
            multiply()
        elif y == "n" or y == "N":
            print("Good bye!\n------------------------------------------------------------------")
        else:
            exit


# Power function
def power():
    try:
        num1, num2 = float(input("Enter first number: ")), float(input("Enter second number: "))
        result = num1 ** num2
        print("The answer: ", result, "\n")
        del (result)
    except:
        print("An error ooccured!")
    finally:
        a = input("do you want continue? (y/n) ")
        if a == "y" or a == "Y":
            power()
        elif a == "n" or a == "N":
            print("Good bye!\n------------------------------------------------------------------")
        else:
            exit


# Square root function
def square_root():
    try:
        num1 = float(input("Enter Your number: "))
        result = sqrt(num1)
        print("The answer: ", result)
    except:
        print("An error ooccured!")
    finally:
        b = input("do you want continue? (y/n) ")
        if b == "y" or b == "Y":
            square_root()
        elif b == "n" or b == "N":
            print("Good bye!\n------------------------------------------------------------------")
        else:
            exit()


# Base codes
while True:
    options()
    '''try:'''
    u_in = input("Enter Your command: ")
    if u_in == "exit" or u_in == "Exit" or u_in == "quit" or u_in == "Quit" or u_in == "n" or u_in == "N":
        print("Good bye!\n------------------------------------------------------------------")
        break
    elif u_in == "+":
        add()
    elif u_in == "-":
        subtract()
    elif u_in == "*":
        multiply()
    elif u_in == "/":
        divide()
    elif u_in == "**":
        power()
    elif u_in == "&":
        square_root()
    else:
        print("check your input!\n")
        break
    '''except:
        print("An error occurred!")

        # Show all errors
        break'''
