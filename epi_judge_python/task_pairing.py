import collections

from test_framework import generic_test

PairedTasks = collections.namedtuple('PairedTasks', ('task_1', 'task_2'))


def optimum_task_assignment(task_durations):
    task_durations.sort()

    for i in range(len(task_durations) // 2):
        print(i, ~i)

    return [PairedTasks(task_durations[i], task_durations[~i])
            for i in range(len(task_durations) // 2)]


if __name__ == '__main__':

    optimum_task_assignment([1, 2, 3, 4, 5, 6, 7, 8])

    # exit(
    #     generic_test.generic_test_main("task_pairing.py", 'task_pairing.tsv',
    #                                    optimum_task_assignment))
