#!/bin/python3

import sys
from copy import deepcopy


def possible_move(start, row, col):
    global end
    next = (start[0] + row, start[1] + col)
    if ((next[0] >= 0) and (next[0] <= end[0]) and
            (next[1] >= 0) and (next[1] <= end[1])):
        return next
    else:
        return None


def compute(row, col, start, counter, mat):
    global end, count
    if (counter >= min(count)):
        return
    # print("compute(" + str(row) + ", " + str(col) +
    #      ", " + str(start) + ", " + str(counter) + ")")
    mat[start[0]][start[1]] = 1
    for i in range(4):
        col *= -1
        if (i == 2):
            row *= -1
        for j in range(2):
            next = possible_move(start, row, col)
            if next:
                #print("next:" + str(next))
                if (next == end):
                    count.append(counter)
                    #print("target: " + str(next))
                elif mat[next[0]][next[1]] == 1:
                    #print("hit once before")
                    pass
                else:
                    compute(row, col, next, counter + 1, deepcopy(mat))
            row, col = col, row


out = []
mat = []
n = int(input())
start = (0, 0)
end = (n - 1, n - 1)
count = [sys.maxsize]
for i in range(n - 1):
    out.append([0] * (n - 1))
for i in range(n):
    mat.append([0] * n)
for i in range(n - 1):
    for j in range(n - 1):
        if out[i][j] == 0:
            compute(i + 1, j + 1, start, 1, deepcopy(mat))
            out[i][j] = out[j][i] = - \
                1 if min(count) == sys.maxsize else min(count)
            count = [sys.maxsize]
        #print("out[" + str(i) + "][" + str(j) + "] : " + str(out[i][j]))
for i in range(n - 1):
    print(*out[i])
