import os


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b


# export ENABLE_ADVANCED=True
def exponentiate(a, b):
    if os.getenv('ENABLE_ADVANCED'):
        return a ** b
    else:
        raise KeyError("Advanced mode is not enabled.")
