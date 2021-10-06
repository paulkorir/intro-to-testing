"""
Here is a simple module that solves quadratic equations.
I will use it to demonstrate how to write unit tests.
The module tests.py has all the tests for the functions here.


We can run this module as follows:

python main.py 1 2 1
"""

import math
import os
import sys


def solve(a, b, c):
    """Solve a quadratic equation from the three coefficients

    :param float
    """
    discriminant = b ** 2 - 4 * a * c
    if discriminant >= 0:
        x1 = (-b + math.sqrt(discriminant)) / 2 / a
        x2 = (-b - math.sqrt(discriminant)) / 2 / a
    else:
        x1 = complex(-b / 2 / a, math.sqrt(-discriminant) / 2 / a)
        x2 = complex(-b / 2 / a, -math.sqrt(-discriminant) / 2 / a)
    return x1, x2


def main():
    try:
        a = float(sys.argv[1])
        b = float(sys.argv[2])
        c = float(sys.argv[3])
    except IndexError:
        print(f"usage: ./main.py a b c", file=sys.stderr)
        return os.EX_USAGE
    x1, x2 = solve(a, b, c)
    print(f"Solution for the quadratic equation {a}*x^2{b:+}*x{c:+} = 0")
    print(f"x1 = {x1}")
    print(f"x2 = {x2}")
    return os.EX_OK


if __name__ == "__main__":
    sys.exit(main())
