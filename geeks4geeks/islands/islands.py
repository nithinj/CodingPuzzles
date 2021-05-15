#!/bin/python3


def account_island(mat, i, j, m, n):
        if (i < 0) or (i >= m) or (j < 0) or (j >= n):
                return
        if (mat[i][j] == -1 or mat[i][j] == 0):
                return
        if mat[i][j] == 1:
                mat[i][j] = -1
                account_island(mat, i + 1, j, m, n)
                account_island(mat, i - 1, j, m, n)
                account_island(mat, i, j + 1, m, n)
                account_island(mat, i, j - 1, m, n)
                account_island(mat, i - 1, j - 1, m, n)
                account_island(mat, i + 1, j + 1, m, n)
                account_island(mat, i + 1, j - 1, m, n)
                account_island(mat, i - 1, j + 1, m, n)


if __name__ == '__main__':

    m = int(input())
    n = int(input())
    mat = []
    for _ in range(m):
            mat.append(list(map(int, input())))

    islands = 0
    for i in range(m):
            for j in range(n):
                    if (mat[i][j] == 1):
                            islands += 1
                            account_island(mat, i, j, m, n)
    print(str(islands))