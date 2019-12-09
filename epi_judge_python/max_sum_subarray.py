from test_framework import generic_test


def find_maximum_subarray(A):

    max_end = max_seen = 0

    for i in range(len(A)):
        max_end = max(max_end + A[i], A[i])
        max_seen = max(max_seen, max_end)

    return max_seen


def find_maximum_subarray_2(A):
    max_end = 0
    max_cur = 0

    for i in range(len(A)):
        max_cur = max(A[i], max_cur + A[i])
        max_end = max(max_end, max_cur)

    return max_end


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("max_sum_subarray.py",
                                       'max_sum_subarray.tsv',
                                       find_maximum_subarray_2))
