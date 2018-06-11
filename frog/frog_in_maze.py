from sys import stdin
import copy
import collections

TUNNEL = 'T'
OBSTACLE = '#'
START = 'A'
MINE = '*'
EXIT = '%'
FREE = 'O'
VISITED = 'V'

success_cases = 0
failed_cases = 0
success_path = []
failed_path = []
DEBUG = 1


def am_I_stuck(row, col, matrix):
    blocked = 1
    if ((row + 1 < n) and (matrix[row + 1][col] != OBSTACLE)):
        blocked = 0
    if ((row - 1 >= 0) and (matrix[row - 1][col] != OBSTACLE)):
        blocked = 0
    if ((col + 1 < m) and (matrix[row][col + 1] != OBSTACLE)):
        blocked = 0
    if ((col - 1 >= 0) and (matrix[row][col - 1] != OBSTACLE)):
        blocked = 0
    return blocked


def go_left(row, col, matrix, path):
    if ((row - 1 >= 0)):
        find_exit(row - 1, col, 0, matrix, path)


def go_right(row, col, matrix, path):
    if (row + 1 < n):
        find_exit(row + 1, col, 0, matrix, path)


def go_up(row, col, matrix, path):
    if (col + 1 < m):
        find_exit(row, col + 1, 0, matrix, path)


def go_down(row, col, matrix, path):
    if (col - 1 >= 0):
        find_exit(row, col - 1, 0, matrix, path)


def update_state(state, path):
    global success_cases, success_path, failed_cases, failed_path
    if state == EXIT:
        coll = collections.Counter(path)
        for l in success_path:
            #print("path:" + str(path) + ", l:" +
             #     str(l))
            if collections.Counter(l) == coll:
                return
        success_cases = success_cases + 1
        success_path.append(path)
        if (DEBUG):
            print("success")
        return
    if state == MINE:
        coll = collections.Counter(path)
        for l in failed_path:
            #print("path:" + str(path) + ", l:" +
             #     str(l))
            if collections.Counter(l) == coll:
                return
        failed_cases = failed_cases + 1
        failed_path.append(path)
        if (DEBUG):
            print("failed")
        return


def find_exit(row, col, prev_tunnel, matrix, path):
    global n, m, DEBUG

    if ((matrix[row][col] == OBSTACLE) or (matrix[row][col] == VISITED)):
        return

    if (DEBUG):
        print("find_exit:row:" + str(row) + "col:" + str(col) + "prev_tunnel:" +
              str(prev_tunnel) + "matrix[row][col]:" + str(matrix[row][col]))

    path = copy.deepcopy(path)
    path.append(row * m + col)

    if (matrix[row][col] == EXIT):
        update_state(EXIT, path)
        return

    if (matrix[row][col] == MINE):
        update_state(MINE, path)
        return

    matrix = copy.deepcopy(matrix)
    if ((matrix[row][col] == TUNNEL) and (prev_tunnel == 0)):
        matrix[row][col] = VISITED
        find_exit(tunnel_dict[row * m + col][0],
                  tunnel_dict[row * m + col][1], 1, matrix, path)
        return

    if ((matrix[row][col] == FREE) or (matrix[row][col] == START) or
            ((matrix[row][col] == TUNNEL) and (prev_tunnel == 1))):
        if (matrix[row][col] != TUNNEL):
            matrix[row][col] = VISITED
        if am_I_stuck(row, col, matrix):
            update_state(MINE, path)
            return
        go_left(row, col, matrix, path)
        go_right(row, col, matrix, path)
        go_up(row, col, matrix, path)
        go_down(row, col, matrix, path)


inp = stdin.readline().split()
inp = [int(x) for x in inp]
(n, m, k) = (inp[0], inp[1], inp[2])
matrix = []
tunnel_dict = {}
for i in range(n):
    matrix.append(list(stdin.readline())[:-1])
for i in range(k):
    tunnel = stdin.readline().split()
    tunnel = [int(x) - 1 for x in tunnel]
    matrix[tunnel[0]][tunnel[1]] = TUNNEL
    matrix[tunnel[2]][tunnel[3]] = TUNNEL
    tunnel_dict[(tunnel[0]) * m + tunnel[1]] = [tunnel[2], tunnel[3]]
    tunnel_dict[(tunnel[2]) * m + tunnel[3]] = [tunnel[0], tunnel[1]]
found = 0
for i in range(n):
    for j in range(m):
        if matrix[i][j] == START:
            find_exit(i, j, 0, matrix, [])
            found = 1
            break
    if found:
        break
if (DEBUG):
    print("success_cases:" + str(success_cases) +
          ", failed_cases:" + str(failed_cases))
if (success_cases == 0):
    print(str(success_cases))
else:
    print(str(success_cases / (success_cases + failed_cases)))
