#!/bin/python3

import sys
from copy import deepcopy
from collections import deque
from math import log


def possible_move(next):
    global end
    if ((next[0] >= 0) and (next[0] <= end[0]) and
            (next[1] >= 0) and (next[1] <= end[1])):
        return next
    else:
        return None


def compute(row, col, mat):
    global end

    que = deque()
    que.append((0, 0))
    que.append(None)
    level = 0
    while(len(que) > 0):
        start = que.popleft()

        if(start == None):
            level += 1
            que.append(None)
            if(que[0] == None):
                break
            # You are encountering two consecutive `None` means, you visited
            # all the nodes.
            else:
                continue

        if (start == end):
            return level
        elif mat[start[0]][start[1]] == 1:
            # hit once before
            pass
        else:
            mat[start[0]][start[1]] = 1
            if (row != col):
                next_list = [(start[0] + row, start[1] + col), (start[0] + row, start[1] - col), (start[0] - row, start[1] + col), (start[0] - row, start[1] - col),
                             (start[0] + col, start[1] + row), (start[0] + col, start[1] - row), (start[0] - col, start[1] + row), (start[0] - col, start[1] - row)]
            else:
                next_list = [(start[0] + row, start[1] + col), (start[0] + row, start[1] - col),
                             (start[0] - row, start[1] + col), (start[0] - row, start[1] - col)]
            for next in next_list:
                if (possible_move(next)):
                    que.append(next)
    return -1


out = []
mat = []
n = int(input())
end = (n - 1, n - 1)
for i in range(n - 1):
    out.append([0] * (n - 1))
for i in range(n):
    mat.append([0] * n)
for i in range(n - 1):
    for j in range(n - 1):
        if out[i][j] == 0:
            out[i][j] = out[j][i] = compute(i + 1, j + 1, deepcopy(mat))
for i in range(n - 1):
    print(*out[i])
