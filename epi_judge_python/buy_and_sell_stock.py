from test_framework import generic_test


def buy_and_sell_stock_once(prices):
    # TODO - you fill in here.
    min_so_far = prices[0]
    max_profit = 0

    for i in range(1, len(prices)):
        min_so_far = min(min_so_far, prices[i])
        max_profit = max(max_profit, prices[i]-min_so_far)

    return max_profit


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("buy_and_sell_stock.py",
                                       "buy_and_sell_stock.tsv",
                                       buy_and_sell_stock_once))
