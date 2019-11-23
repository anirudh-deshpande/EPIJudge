from test_framework import generic_test
from test_framework.test_failure import TestFailure

import collections

class Stack:

    ElementWithCached = collections.namedtuple("ElementWithMaxCached", ("element", "max"))

    def __init__(self):
        self.element_with_max_cached = []

    def empty(self):
        return len(self.element_with_max_cached) == 0

    def max(self):
        return self.element_with_max_cached[-1].max

    def pop(self):
        if self.element_with_max_cached:
            return self.element_with_max_cached.pop().element

        return 0

    def push(self, x):
        self.element_with_max_cached.append(
            self.ElementWithCached(x,
                                 x if not self.element_with_max_cached
                                 else max(x, self.element_with_max_cached[-1].max))
        )
        return


def stack_tester(ops):
    try:
        s = Stack()

        for (op, arg) in ops:
            if op == 'Stack':
                s = Stack()
            elif op == 'push':
                s.push(arg)
            elif op == 'pop':
                result = s.pop()
                if result != arg:
                    raise TestFailure(
                        "Pop: expected " + str(arg) + ", got " + str(result))
            elif op == 'max':
                result = s.max()
                if result != arg:
                    raise TestFailure(
                        "Max: expected " + str(arg) + ", got " + str(result))
            elif op == 'empty':
                result = int(s.empty())
                if result != arg:
                    raise TestFailure(
                        "Empty: expected " + str(arg) + ", got " + str(result))
            else:
                raise RuntimeError("Unsupported stack operation: " + op)
    except IndexError:
        raise TestFailure('Unexpected IndexError exception')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("stack_with_max.py",
                                       'stack_with_max.tsv', stack_tester))
