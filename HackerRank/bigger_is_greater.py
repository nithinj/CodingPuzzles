#!/bin/python3


def biggerIsGreater(w):
    l = len(w)
    rev = w[::-1]
    for i in range(1, l):
        for j in range(i + 1):
            if rev[j] > rev[i]:
                [rev[i], rev[j]] = [rev[j], rev[i]]
                res = sorted(rev[0: i], reverse=True) + rev[i:]
                return ''.join(res[::-1])
    return "no answer"

if __name__ == '__main__':

    T = int(input())
    for T_itr in range(T):
        w = list(input())
        result = biggerIsGreater(w)
        print(result)
