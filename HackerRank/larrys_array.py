#!/bin/python3


def larrysArray(A):
    sorted_A = sorted(A)
    dup_arr = []
    for elm in sorted_A:
        while elm != A[0]:
            loc = A.index(elm)
            if len(A) < 3:
                if sorted(A) == A:
                    return "YES"
                else:
                    return "NO"
            elif loc == 1:
                A.insert(loc + 2, A[0])
                del A[0]
            else:
                A.insert(loc + 1, A[loc - 2])
                del A[loc - 2]
        dup_arr.append(A[0])
        del A[0]
    if dup_arr == sorted_A:
        return "YES"


if __name__ == '__main__':

    t = int(input())
    for t_itr in range(t):
        n = int(input())
        A = list(map(int, input().rstrip().split()))
        result = larrysArray(A)
        print(result)
