#!/bin/python3


def sansaXor(arr):
    if len(arr) % 2 == 0:
        return 0
    xor = 0
    for i in range(0, len(arr), 2):
        xor ^= arr[i]
    return xor

if __name__ == '__main__':
    t = int(input())
    for t_itr in range(t):
        n = int(input())
        arr = list(map(int, input().rstrip().split()))
        result = sansaXor(arr)
        print(str(result))
