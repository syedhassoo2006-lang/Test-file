# Simple Buggy Calculator

def add(a, b):
    return a + b

def subtract(a, b) # Bug 1: Missing colon
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

num1 = input("Enter first number: ")
num2 = input("Enter second number: ")
operation = input("Choose operation (+, -, *, /): ")

if operation == "+":
    result = add(num1, num2) # Bug 2: Strings concatenated instead of added
elif operation == "-":
    result = subtract(num1, num2)
elif operation == "*":
    result = multiply(num1, num2)
elif operation == "/":
    result = divide(num1, num2) # Bug 3: Division by zero crashes the program
else:
    print("Invalid operator")

print("Result is: " + result) # Bug 4: NameError if operation is invalid (result undefined)