from test_framework import generic_test


def parity(x):
    """
    Approach 0, 1 => O(n) runtime
    """
    # Approach 0
    # count = 0
    #
    # while x:
    #     if x & 1 != 0:
    #         count += 1
    #     x = x >> 1

    # return count % 2

    # Approach 1
    # result1 = 0
    #
    # while x:
    #     result1 ^= (x & 1)
    #     x >>= 1
    #
    # return result1

    """
    Approach 2: O(k) runtime, k = no. of set bits
    """
    # Approach 2
    # result2 = 0
    #
    # while x:
    #     result2 ^= 1
    #     x = x & (x - 1)

    # return result2

    """
    Approach 3: O(log n) runtime.
    """
    n = 64
    while n > 1:
        x ^= x >> int(n/2)
        n = int(n/2)

    return x & 0x1


if __name__ == '__main__':
    exit(generic_test.generic_test_main("parity.py", 'parity.tsv', parity))
