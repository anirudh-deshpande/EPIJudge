from test_framework import generic_test
import heapq
import collections

# (cur_val, array, cur_index, length)

FileMetadata = collections.namedtuple("FileMetadata", ("cur_val", "array", "cur_index", "length"))
heap_list = []

def merge_sorted_arrays(sorted_arrays):

    for array in sorted_arrays:
        if array:
            heapq.heappush(heap_list, FileMetadata(array[0], array, 0, len(array)))

    result = []

    while heap_list:
        min_file = heapq.heappop(heap_list)
        result.append(min_file.cur_val)

        if min_file.cur_index < min_file.length-1:
            next_index = min_file.cur_index+1
            heapq.heappush(heap_list,
                           FileMetadata(
                               min_file.array[next_index],
                               min_file.array,
                               next_index,
                               min_file.length
                           ))

    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("sorted_arrays_merge.py",
                                       "sorted_arrays_merge.tsv",
                                       merge_sorted_arrays))
