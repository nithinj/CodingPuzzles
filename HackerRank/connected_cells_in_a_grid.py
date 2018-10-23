#!/bin/python3


def calc(row, col):
    global n, m, matrix

    if ((row >= 0) and (row < n) and (col >= 0) and (col < m) and
            matrix[row][col] and not connectedCell.track[row][col]):
        connectedCell.track[row][col] = 1
        return (1 + calc(row + 1, col) + calc(row - 1, col) +
                calc(row, col + 1) + calc(row, col - 1) +
                calc(row + 1, col + 1) + calc(row - 1, col - 1) +
                calc(row + 1, col - 1) + calc(row - 1, col + 1))
    return 0


def connectedCell(matrix):
    global n, m
    connectedCell.track = []

    for _ in range(n):
        connectedCell.track.append([0] * m)

    res = []
    for i in range(n):
        for j in range(m):
            count = calc(i, j)
            if count:
                res.append(count)
    return max(res)


if __name__ == '__main__':
    n = int(input())
    m = int(input())
    matrix = []
    for _ in range(n):
        matrix.append(list(map(int, input().rstrip().split())))
    result = connectedCell(matrix)
    print(str(result))
