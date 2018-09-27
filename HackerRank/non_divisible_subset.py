#!/bin/python3

DBG = 0


def nonDivisibleSubset(k, S):
    remainders = [0] * k
    S = list(set(S))
    if DBG:
        print(str(S))
    for num in S:
        remainders[int(num % k)] += 1
    if DBG:
        print(str(remainders))
    total = 0
    i = 0
    j = len(remainders)
    while i <= j:
        if i == 0 or (i == j):
            if remainders[i]:
                total += 1
        else:
            if (remainders[i] > remainders[j]):
                total += remainders[i]
            else:
                total += remainders[j]
        i += 1
        j -= 1
    return total

nk = input().split()

n = int(nk[0])

k = int(nk[1])

S = list(map(int, input().rstrip().split()))

result = nonDivisibleSubset(k, S)

print(str(result))
