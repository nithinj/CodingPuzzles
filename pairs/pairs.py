#!/bin/python3


def pairs(k, arr):
    global n
    dic = {}
    count = 0

    for num in arr:
        if num in dic:
            dic[num] += 1
        else:
            dic[num] = 1

    for num in arr:
        if num + k in dic:
            count += dic[num + k]
    return count


if __name__ == '__main__':
    nk = input().split()
    n = int(nk[0])
    k = int(nk[1])
    arr = list(map(int, input().rstrip().split()))
    result = pairs(k, arr)
    print(str(result))
