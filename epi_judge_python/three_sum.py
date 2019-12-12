from test_framework import generic_test


def has_three_sum_1(A, t):

    for i in range(len(A)):
        for j in range(len(A)):
            for k in range(len(A)):
                if A[i] + A[j] + A[k] == t:
                    return True

    return False


def has_three_sum_2(A, t):

    a_set = set(A)

    for i in range(len(A)):
        for j in range(len(A)):
            two_sum = A[i]+A[j]
            if t - two_sum in a_set:
                return True

    return False


def has_three_sum_3(A, t):
    A.sort()

    for i in range(len(A)):
        low = i
        high = len(A) - 1

        while low <= high:
            if A[i] + A[low] + A[high] == t:
                return True
            elif A[i] + A[low] + A[high] < t:
                low += 1
            else:
                high -= 1

    return False    


if __name__ == '__main__':

    exit(
        generic_test.generic_test_main("three_sum.py", "three_sum.tsv",
                                       has_three_sum_3))