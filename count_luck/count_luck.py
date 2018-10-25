#!/bin/python3


def possible_move(mat, x, y):
    global n, m

    if (x >= 0 and x < n and y >= 0 and y < m and (mat[x][y] == '.' or
                                                   mat[x][y] == '*')):
        return 1
    return 0


def count_split(x, y, count, mat):
    global n, m, k

    if (x >= 0 and x < n and y >= 0 and y < m and count <= k):
        if mat[x][y] == '*':
            return count
        elif mat[x][y] == '.' or mat[x][y] == 'M':
            if (possible_move(mat, x + 1, y) + possible_move(mat, x, y + 1) +
                    possible_move(mat, x - 1, y) +
                    possible_move(mat, x, y - 1)) > 1:
                mat[x][y] = '1'
                count += 1
            else:
                mat[x][y] = '0'
            return min(count_split(x + 1, y, count, mat),
                       count_split(x, y + 1, count, mat),
                       count_split(x - 1, y, count, mat),
                       count_split(x, y - 1, count, mat))
    return 99999


def countLuck(matrix, k):
    global n, m

    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 'M':
                res = count_split(i, j, 0, matrix)
                break
    #print(str(res))
    if res == k:
        return "Impressed"
    return "Oops!"


if __name__ == '__main__':
    t = int(input())
    for t_itr in range(t):
        nm = input().split()
        n = int(nm[0])
        m = int(nm[1])
        matrix = []
        for _ in range(n):
            matrix_item = list(input())
            matrix.append(matrix_item)
        k = int(input())
        result = countLuck(matrix, k)
        print(result)
