from test_framework import generic_test


def intersect_two_sorted_arrays(A, B):
    m, n = len(A), len(B)
    i, j = 0, 0
    res = []

    while i < m and j < n:
        while i < m and j < n and A[i] < B[j]:
            i += 1
        if i < m and j < n and A[i] == B[j]:
            res.append(A[i])

            tmp = A[i]
            while i < m and j < n and A[i] == tmp:
                i += 1

            while i < m and j < n and B[j] == tmp:
                j += 1

        while j < n and i < m and B[j] < A[i]:
            j += 1

    return res

def intersect_two_sorted_arrays_2(A, B):
    m, n = len(A), len(B)
    i, j = 0, 0
    res = []

    while i < m and j < n:
        if A[i] == B[j]:
            if i == 0 or A[i-1] != A[i]:
                res.append(A[i])
            i += 1
            j += 1
        elif A[i] < B[j]:
            i += 1
        else:
            j += 1

    return res


if __name__ == '__main__':
    generic_test.generic_test_main("intersect_sorted_arrays.py",
                                   'intersect_sorted_arrays.tsv',
                                   intersect_two_sorted_arrays_2)
    exit(
        generic_test.generic_test_main("intersect_sorted_arrays.py",
                                       'intersect_sorted_arrays.tsv',
                                       intersect_two_sorted_arrays))
