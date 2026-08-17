# Math functions

def add(*numbers):
    return sum(numbers)

def subtract(first, *numbers):
    result = first

    for number in numbers:
        result -= number

    return result

def multiply(*numbers):
    result = 1

    for number in numbers:
        result *= number

    return result

def divide(first, *numbers):
    result = first

    for number in numbers:
        if number == 0:
            raise ZeroDivisionError

        result /= number

    return result