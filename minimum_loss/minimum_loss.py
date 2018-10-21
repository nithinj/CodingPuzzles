#!/bin/python3

import sys


def minimumLoss(price):
    global n
    min_list = []
    myDict = {}

    for i in range(n):
        myDict[price[i]] = i
    minCost = 10**10
    nums = sorted(myDict)
    for i in range(1, n):
        if (nums[i] - nums[i - 1] < minCost) and (myDict[nums[i]] < myDict[nums[i - 1]]):
            minCost = nums[i] - nums[i - 1]

    return minCost


if __name__ == '__main__':
    n = int(input())
    price = list(map(int, input().rstrip().split()))
    result = minimumLoss(price)
    print(str(result))
