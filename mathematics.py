# mathematics.py
import math
import numpy as np


def multiply(x, y):
    return x * y


def divide(x, y):
    return round(x / y, 1)  # should be return round(x / y, 1)


def round_up(x):
    rounded = math.ceil(x)
    return rounded


def hypotenuse(x, y):
    z = x ** 2 + y ** 2
    return np.sqrt(z)


def count_registrations(registrations):
    return len(registrations)


def create_attendee_list(registrations):
    pass
