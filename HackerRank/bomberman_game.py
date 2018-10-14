#!/bin/python3
from copy import deepcopy


def bomberMan(n, grid):
    global r, c

    if n == 0 or n == 1:
        return grid
    if (n - 3) % 2 == 1 or n == 2:
        for row in grid:
            for i in range(c):
                row[i] = 'O'
        return grid
    result = deepcopy(grid)
    states = []
    for itr in range(int((n - 3) / 2) + 1):
        grid = deepcopy(result)
        for i in range(r):
            for j in range(c):
                if grid[i][j] == 'O':
                    result[i][j] = '1'
                    if i + 1 < r:
                        result[i + 1][j] = '1'
                    if i - 1 >= 0:
                        result[i - 1][j] = '1'
                    if j + 1 < c:
                        result[i][j + 1] = '1'
                    if j - 1 >= 0:
                        result[i][j - 1] = '1'
        for i in range(r):
            for j in range(c):
                if result[i][j] == '.':
                    result[i][j] = 'O'
                elif result[i][j] == '1':
                    result[i][j] = '.'
        states.append(deepcopy(result))
        if itr != 0 and result == states[0]:
            return states[int((n - 3) / 2) % itr]
    return result

if __name__ == '__main__':
    rcn = input().split()
    r = int(rcn[0])
    c = int(rcn[1])
    n = int(rcn[2])
    grid = []
    for _ in range(r):
        grid_item = list(input())
        grid.append(grid_item)
    result = bomberMan(n, grid)
    result = [''.join(x) for x in result]
    print('\n'.join(result))
