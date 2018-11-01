#!/bin/python3


def stockmax(prices):
    profit = 0
    while prices:
        max_val = max(prices)
        ind = prices.index(max_val)
        profit += (ind * max_val) - sum(prices[:ind])
        prices = prices[ind + 1:]
    return profit


if __name__ == '__main__':
    t = int(input())
    for t_itr in range(t):
        n = int(input())
        prices = list(map(int, input().rstrip().split()))

        result = stockmax(prices)
        print(str(result))
