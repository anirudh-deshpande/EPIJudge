from test_framework import generic_test

import collections

TreeBalanceHeight = collections.namedtuple("TreeBalanceHeight", ("balance", "height"))

def is_balanced(tree):
    if not tree:
        return TreeBalanceHeight(True, 0)

    left_balance_height = is_balanced(tree.left)
    right_balance_height = is_balanced(tree.right)

    cur_balance = left_balance_height.balance and right_balance_height.balance
    if abs(left_balance_height.height - right_balance_height.height) > 1:
        cur_balance = False

    cur_height = max(left_balance_height.height, right_balance_height.height) + 1

    return TreeBalanceHeight(cur_balance, cur_height)


def is_balanced_binary_tree(tree):
    tree_balance_height = is_balanced(tree)
    return tree_balance_height.balance


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_tree_balanced.py",
                                       'is_tree_balanced.tsv',
                                       is_balanced_binary_tree))
