import functools

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

NUM_PEGS = 4


def compute_tower_hanoi(num_rings):
    def tower_of_hanoi(num_rings, from_peg, to_peg, aux_peg, movements, pegs):
        if num_rings == 1:
            movements.append([from_peg, to_peg])
            pegs[to_peg].append(pegs[from_peg].pop())
        else:
            tower_of_hanoi(num_rings-1, from_peg, aux_peg, to_peg, movements, pegs)
            movements.append([from_peg, to_peg])
            pegs[to_peg].append(pegs[from_peg].pop())
            tower_of_hanoi(num_rings-1, aux_peg, to_peg, from_peg, movements, pegs)

    movements = []
    pegs = [list(reversed(range(1,num_rings+1)))] + [[] for _ in range(1, NUM_PEGS)]
    tower_of_hanoi(num_rings, 0, 1, 2, movements, pegs)
    return movements

def moves(from_rod, to_rod, rods, movements):
    movements.append([from_rod, to_rod])
    rods[to_rod].append(rods[from_rod].pop())
    # print(movements, rods)

def top_value(rod_index, rods):
    if not rods[rod_index]:
        return float('inf')
    return rods[rod_index][-1]

def compute_tower_hanoi_2(num_rings):
    rods = [list(reversed(range(1, num_rings+1)))] + [[] for _ in range(1, NUM_PEGS)]
    # print(rods)
    movements = []
    next = [1, 2, 0]
    prev = [2, 0, 1]

    num_moves = (1 << num_rings) - 1
    move_smallest = True
    direction = 1 if (num_rings % 2) == 0 else -1
    rod_min = 0

    for i in range(num_moves):
        if move_smallest:
            new_rod_min = (rod_min + direction) % NUM_PEGS
            moves(rod_min, new_rod_min, rods, movements)
            rod_min = new_rod_min
        else:
            if top_value(next[rod_min], rods) > top_value(prev[rod_min], rods):
                moves(prev[rod_min], next[rod_min], rods, movements)
            else:
                moves(next[rod_min], prev[rod_min], rods, movements)

        move_smallest = not move_smallest
    return movements



@enable_executor_hook
def compute_tower_hanoi_wrapper(executor, num_rings):
    pegs = [list(reversed(range(1, num_rings + 1)))] + [[] for _ in range(
        1, NUM_PEGS)]

    result = executor.run(functools.partial(compute_tower_hanoi_2, num_rings))

    for from_peg, to_peg in result:
        if pegs[to_peg] and pegs[from_peg][-1] >= pegs[to_peg][-1]:
            raise TestFailure("Illegal move from {} to {}".format(
                pegs[from_peg][-1], pegs[to_peg][-1]))
        pegs[to_peg].append(pegs[from_peg].pop())
    expected_pegs1 = [[], [], list(reversed(range(1, num_rings + 1)))]
    expected_pegs2 = [[], list(reversed(range(1, num_rings + 1))), []]
    if pegs not in (expected_pegs1, expected_pegs2):
        raise TestFailure("Pegs doesn't place in the right configuration")


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("hanoi.py", 'hanoi.tsv',
                                       compute_tower_hanoi_wrapper))
