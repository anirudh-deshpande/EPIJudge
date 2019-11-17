from test_framework import generic_test


def parity(x):
    # TODO - you fill in here.

    count = 0
    while x:
        if x & 1 != 0:
            count += 1
        x = x >> 1

    return count % 2


if __name__ == '__main__':
    exit(generic_test.generic_test_main("parity.py", 'parity.tsv', parity))
