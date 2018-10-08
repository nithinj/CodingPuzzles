#!/bin/python3

import time


def absolutePermutation(n, k):
    res = []
    temp = k

    if k == 0:
        for i in range(1, n + 1):
            res.append(i)
    elif n % (2 * k) == 0:
        for i in range(1, n + 1):
            res.append(i + temp)
            if i % k == 0:
                temp *= -1
    else:
        res = [-1]

    return res


if __name__ == '__main__':

    t = int(input())
    for t_itr in range(t):
        nk = input().split()
        n = int(nk[0])
        k = int(nk[1])
        result = absolutePermutation(n, k)
        print(' '.join(map(str, result)))
