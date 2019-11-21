from test_framework import generic_test
from test_framework.test_failure import TestFailure

import functools
import string

def int_to_string(x):
    if x == 0:                                 # Missed
        return '0'

    is_negative = '-' if x < 0 else ''
    abs_x = abs(x)
    digits = []

    while abs_x != 0:
        reminder = abs_x % 10
        digits.append(chr(reminder+ord('0'))) # 1. For join: Join can only join strings, 2. ord->chr
        abs_x = abs_x // 10

    digits.append(is_negative)
    digits.reverse()

    return ''.join(digits)


def string_to_int(s):
    """
    1. functools.reduce
    Apply a function of two arguments cumulatively to the items of a sequence,
    from left to right, so as to reduce the sequence to a single value.

    2. string.digits == "0123456789"
    similarly, string.ascii_lowercase, ascii_uppercase, ascii_letters, punctuation etc.
    """

    return functools.reduce(
        lambda running_sum, c: running_sum*10 + string.digits.index(c),
        s[1:] if s[0] == '-' else s, 0
    ) * (-1 if s[0] == '-' else 1)


    # is_negative = s[0] == '-'
    # s = s[1:] if is_negative else s
    #
    # decimal = 1
    # int = 0
    #
    # for char in reversed(s):
    #     value = ord(char) - ord('0')
    #     int += value * decimal
    #     decimal *= 10
    #
    # return -int if is_negative else int


def wrapper(x, s):
    if int_to_string(x) != s:
        raise TestFailure("Int to string conversion failed")
    if string_to_int(s) != x:
        raise TestFailure("String to int conversion failed")


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("string_integer_interconversion.py",
                                       'string_integer_interconversion.tsv',
                                       wrapper))
