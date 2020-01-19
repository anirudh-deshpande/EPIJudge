import collections
import functools
import heapq

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

Interval = collections.namedtuple('Interval', ('left', 'right'))


def find_minimum_visits(intervals):
    intervals.sort(key=lambda x:(x.right, x.left))
    last_visit_time, num_visits = float('-inf'), 0

    for interval in intervals:
        if interval.left > last_visit_time:
            last_visit_time = interval.right
            num_visits += 1

    return num_visits


@enable_executor_hook
def find_minimum_visits_wrapper(executor, A):
    A = [Interval(*a) for a in A]
    return executor.run(functools.partial(find_minimum_visits, A))


if __name__ == '__main__':
    # A = [Interval(*a) for a in [[1, 4], [2, 8], [3, 6], [3, 5], [7, 10], [9, 11]]]
    # find_minimum_visits(A)
    exit(
        generic_test.generic_test_main("minimum_points_covering_intervals.py",
                                       'minimum_points_covering_intervals.tsv',
                                       find_minimum_visits_wrapper))
