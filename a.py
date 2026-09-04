```python
# Improved Buggy Calculator

import sys

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        print('Error: Division by zero is not allowed. Please choose another operation.')
        sys.exit(1)

num1 = input('Enter first number: ').strip()
num2 = input('Enter second number: ').strip()
operation = input('Choose operation (+, -, *, /): ').strip()

if operation == '+':
    result = add(num1, num2)
elif operation == '-':
    result = subtract(num1, num2)
elif operation == '*':
    result = multiply(num1, num2)
elif operation == '/':
    result = divide(num1, num2)
else:
    print('Invalid operator')

if result is not None:
    print('Result is: ' + str(result))
```