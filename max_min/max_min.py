#!/bin/python3

import sys


def maxMin(k, arr):
    arr.sort()
    # print(str(arr))
    min_ = sys.maxsize
    for i in range(len(arr) - k + 1):
        diff = arr[i + k - 1] - arr[i]
        if diff < min_:
            min_ = diff
        #print("i:" + str(i) + "min_:" + str(min_))
    return min_


if __name__ == '__main__':
    n = int(input())
    k = int(input())
    arr = []
    for _ in range(n):
        arr_item = int(input())
        arr.append(arr_item)

    result = maxMin(k, arr)
    print(str(result))
