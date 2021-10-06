"""
This module contains the tests for the functions in main.py.
We can run this module as follows:

~$ python -m unittest tests

This the expected output:

....
----------------------------------------------------------------------
Ran 4 tests in 0.000s

OK

Now any time I modify the code I can always run the tests to make sure that the old functionality and new
functionality are supported.
"""

# This is the Python unittest library
# It contains many important tools to run unittests
import unittest

# we import the function to test
from main import solve


class TestSolve(unittest.TestCase):
    """
    This is a class that hosts our test cases. It is a subclass of the unittest.TestCase class.
    Memorise this for now but over time, as you read the library, you will see a beautiful structure
    emerge on how Python has designed this class.

    Notice that the methods of this class all begin with 'test_'.
    This is important for Python to identify them as tests.
    """
    def test_default(self):
        """This is how we write a test method. In this test we want to run a simple
        test on a trivial example i.e. when we know x1,x2 = -1
        These arise when (x+1)(x+1) = x^2+2x+1 = 0
        Therefore, a = 1, b = 2, c = 1
        """
        x1, x2 = solve(1, 2, 1)
        # now we assert that these have the correct values
        # this is a special method to check that values are equal
        self.assertEqual(-1, x1)
        self.assertEqual(-1, x2)

    def test_simple(self):
        """Here is another simple test for x1,x2 = 1
        We know this is the case when (x-1)(x-1) = x^2-2x+1 = 0
        """
        x1, x2 = solve(1, -2, 1)
        self.assertEqual(1, x1)
        self.assertEqual(1, x2)

    def test_exotic(self):
        """Let's try something more exotic: https://www.mathsisfun.com/quadratic-equation-solver.html
        x1 = -3, x2 = 0.5
        whereby
        2x^2 + 5x - 3 = 0
        """
        x1, x2 = solve(2, 5, -3)
        self.assertEqual(0.5, x1)
        self.assertEqual(-3, x2)

    def test_complex(self):
        """Now for something special: a complex solution
        x1 = -0.5 + 0.86602540378444j
        x2 = -0.5 - 0.86602540378444j
        which are the roots of
        x^2 + x + 1 = 0
        """
        x1, x2 = solve(1, 1, 1)
        # Notice that now we use a different assertion method
        self.assertAlmostEqual(complex(-0.5, 0.86602540378444), x1)
        self.assertAlmostEqual(complex(-0.5, -0.86602540378444), x2)
