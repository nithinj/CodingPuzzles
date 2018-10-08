#!/bin/python3


def surfaceArea(A):
    area = len(A) * len(A[0]) * 2
    for i in range(len(A)):
        for j in range(len(A[0])):
            if i - 1 >= 0:
                area += max(0, A[i][j] - A[i - 1][j])
            else:
                area += A[i][j]
            if i + 1 < len(A):
                area += max(0, A[i][j] - A[i + 1][j])
            else:
                area += A[i][j]
            if j - 1 >= 0:
                area += max(0, A[i][j] - A[i][j - 1])
            else:
                area += A[i][j]
            if j + 1 < len(A[0]):
                area += max(0, A[i][j] - A[i][j + 1])
            else:
                area += A[i][j]
    return area

if __name__ == '__main__':

    HW = input().split()
    H = int(HW[0])
    W = int(HW[1])
    A = []
    for _ in range(H):
        A.append(list(map(int, input().rstrip().split())))
    result = surfaceArea(A)
    print(str(result))
