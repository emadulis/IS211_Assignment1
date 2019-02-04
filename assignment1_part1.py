#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Week1 module part1"""


class ListDivideException(Exception):
    """This class raises an Exception"""


def listDivide(numbers, divide=2):
    """This function returns numbers the lists.
    Args:
        numbers(list): a list of numbers
        divide(integer): a divisor integer
        
    Return:
        The number of elements in the numbers list that are divisible by divide.
    Example:
        >>> listDivide([1,2,3,4,5,])
        2
        >>> listDivide([2,4,6,8,10])
        5
        >>> listDivide([30, 54, 63, 98, 100], divide=10)
        2
        >>> listDivide([])
        0
        >>> listDivide([1,2,3,4,5], 1)
        5
    """
    counter = 0
    for number in numbers:
        if number % divide == 0:
            counter += 1
    return counter

def testListDivide():
    """Tests the listDivide function."""
    test_a = listDivide([1, 2, 3, 4, 5])
    test_b = listDivide([2, 4, 6, 8, 10])
    test_c = listDivide([30, 54, 63, 98, 100], divide=10)
    test_d = listDivide([])
    test_e = listDivide([1, 2, 3, 4, 5], 1)

    tests = (test_a, test_b, test_c, test_d, test_e)
    while test_a == int(2):
        while test_b == int(5):
            while test_c == int(2):
                while test_d == int(0):
                    while test_e == int(5):
                        return tests
    else:
        raise ListDivideException('Exception: a number is incorrect')

print(testListDivide())
