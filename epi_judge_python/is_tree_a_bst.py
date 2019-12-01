from test_framework import generic_test

import collections

def is_binary_tree_bst(tree, low_range=float('-inf'), high_range=float('inf')):
    if not tree:
        return True

    if (low_range > tree.data) or (tree.data > high_range): # was not evaluating correct
        return False

    return (is_binary_tree_bst(tree.left, low_range, tree.data)
           and is_binary_tree_bst(tree.right, tree.data, high_range))


def is_binary_tree_bst_1(tree, low_range=float('-inf'), high_range=float('inf')):

    if tree is None:
        return True

    left = is_binary_tree_bst_1(tree.left, low_range, tree.data)

    if (not low_range <= tree.data) or (not tree.data <= high_range):
        return False

    right = is_binary_tree_bst_1(tree.right, tree.data, high_range)

    return left and right


def is_binary_tree_bst_2(node, low_range=float('-inf'), high_range=float('inf')):

    Element = collections.namedtuple("Element", ("node", "low", "high"))

    queue = collections.deque(
        [Element(node, float('-inf'), float('inf'))])

    while queue:
        element = queue.popleft()

        if element.node:
            if element.low > element.node.data or element.node.data > element.high:
                return False

            queue.append(Element(element.node.left, element.low, element.node.data))
            queue.append(Element(element.node.right, element.node.data, element.high))

    return True


if __name__ == '__main__':
    # generic_test.generic_test_main("is_tree_a_bst.py", 'is_tree_a_bst.tsv',
    #                                is_binary_tree_bst)
    exit(
        generic_test.generic_test_main("is_tree_a_bst.py", 'is_tree_a_bst.tsv',
                                       is_binary_tree_bst_2))
