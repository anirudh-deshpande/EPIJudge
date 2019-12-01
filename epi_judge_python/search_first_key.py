from test_framework import generic_test


def search_first_of_k(A, k):
    low, high = 0, len(A) - 1

    ans = -1

    while low <= high:
        mid = low + (high - low) // 2

        if A[mid] == k:
            ans = mid
            high = mid - 1
        if A[mid] < k:
            low = mid + 1
        else:
            high = mid - 1

    return ans


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "search_first_key.py", 'search_first_key.tsv', search_first_of_k))
