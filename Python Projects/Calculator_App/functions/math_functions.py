# Math functions
import math

# Basic
def add(*numbers):
    return sum(numbers)

def subtract(first, *numbers):
    result = first

    for number in numbers:
        result -= number

    return result

def multiply(*numbers):
    return math.prod(numbers)

def divide(first, *numbers):
    result = first

    for number in numbers:
        if number == 0:
            raise ZeroDivisionError

        result /= number

    return result

# Advanced
def square_root(number):
    return math.sqrt(number)

def power(base, exponent):
    return base ** exponent

def percent(number, percent):
    return number * (percent/100)

def absolute_value(number):
    return abs(number)