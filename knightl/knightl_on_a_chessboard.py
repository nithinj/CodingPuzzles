#!/bin/python3

import sys


def possible_move(start, row, col):
    global end
    next = (start[0] + row, start[1] + col)
    if ((next[0] >= 0) and (next[0] <= end[0]) and
            ((next[1] >= 0) and (next[1] <= end[1]))):
        return next
    else:
        return None


def compute(row, col, start, counter, mat):
    print("compute(" + str(row) + ", " + str(col) +
          ", " + str(start) + ", " + str(counter) + ")")
    global end, count
    mat[start[0]][start[1]] = 1
    for i in range(4):
        col *= -1
        if (i > 1 and row > 0):
            row *= -1
        for j in range(2):
            next = possible_move(start, row, col)
            print("next:" + str(next))
            if next:
                if (next == end):
                    count.append(counter)
                    print("target")
                elif mat[next[0]][next[1]] == 1:
                    print("hit once before")
                    return
                else:
                    print("computing again!")
                    compute(row, col, next, counter + 1, mat)
            row, col = col, row


out = []
mat = []
n = int(input())
start = (0, 0)
end = (n - 1, n - 1)
count = [100]
for i in range(n - 1):
    out.append([0] * (n - 1))
for i in range(n):
    mat.append([0] * n)
for i in range(n - 1):
    for j in range(n - 1):
        if out[i][j] == 0:
            compute(i + 1, j + 1, start, 1, mat)
            out[i][j] = out[j][i] = -1 if min(count) == 100 else min(count)
            count = [100]
for i in range(n - 1):
    print(*out[i])
