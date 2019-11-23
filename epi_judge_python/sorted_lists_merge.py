from test_framework import generic_test

from epi_judge_python.list_node import ListNode


def merge_two_sorted_lists_1(L1, L2):
    cur_1 = L1
    cur_2 = L2
    new_head = None
    new_cur = None

    if cur_1 == None:
        return cur_2

    if cur_2 == None:
        return cur_1

    while cur_1 != None and cur_2 != None:
        if cur_1.data < cur_2.data:
            if not new_head:
                new_head = cur_1
            else:
                new_cur.next = cur_1

            new_cur = cur_1
            cur_1 = cur_1.next
        else:
            if not new_head:
                new_head = cur_2
            else:
                new_cur.next = cur_2

            new_cur = cur_2
            cur_2 = cur_2.next

    if cur_1 == None:
        new_cur.next = cur_2

    if cur_2 == None:
        new_cur.next = cur_1

    return new_head


def merge_two_sorted_lists(L1, L2):
    dummy_head = tail = ListNode()

    while L1 and L2:
        if L1.data < L2.data:
            tail.next, L1 = L1, L1.next
        else:
            tail.next, L2 = L2, L2.next
        tail = tail.next

    tail.next = L1 or L2

    return dummy_head.next





if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("sorted_lists_merge.py",
                                       'sorted_lists_merge.tsv',
                                       merge_two_sorted_lists))
