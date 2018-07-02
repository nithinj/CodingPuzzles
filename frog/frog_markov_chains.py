from sys import stdin
import numpy as np
import copy

np.set_printoptions(threshold='nan')
out_format = "%.3f"

TUNNEL = 'T'
OBSTACLE = '#'
START = 'A'
MINE = '*'
EXIT = '%'
FREE = 'O'
VISITED = 'V'


def am_I_stuck(row, col):
    global matrix
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


def calc_prob(row, col):
    global matrix, m
    prob_dict = {}
    chances = 0.0
    if matrix[row][col] == TUNNEL:
        prob_dict[index_map[tunnel_dict[row * m + col]]] = 1
    else:
        if ((row - 1 >= 0) and (matrix[row - 1][col] != OBSTACLE)):
            chances = chances + 1
            prob_dict[index(row - 1, col)] = -1
        if (row + 1 < n) and (matrix[row + 1][col] != OBSTACLE):
            chances = chances + 1
            prob_dict[index(row + 1, col)] = -1
        if (col + 1 < m) and (matrix[row][col + 1] != OBSTACLE):
            chances = chances + 1
            prob_dict[index(row, col + 1)] = -1
        if (col - 1 >= 0) and (matrix[row][col - 1] != OBSTACLE):
            chances = chances + 1
            prob_dict[index(row, col - 1)] = -1
    total_chance = 1.0
    #if matrix[row][col] == TUNNEL:
     #   prob_dict[index_map[tunnel_dict[row * m + col]]] = \
      #      chances / (chances + 1)
       # total_chance = 1 - (chances / (chances + 1))
    for key, val in prob_dict.items():
        if val == -1:
            prob_dict[key] = total_chance / chances

        # print("row:"+str(row)+"col:"+str(col)+"matrix[row][col]:"+str(matrix[row][col])+"prob_dict[key]:"+str(prob_dict[key]))
    return prob_dict


def index(row, col):
    global index_map, m
    return(index_map[row * m + col])


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
    tunnel_dict[(tunnel[0]) * m + tunnel[1]] = tunnel[2] * m + tunnel[3]
    tunnel_dict[(tunnel[2]) * m + tunnel[3]] = tunnel[0] * m + tunnel[1]

index_map = {}
counter = 0
for row in range(n):
    for col in range(m):
        if (matrix[row][col] != OBSTACLE):
            index_map[row * m + col] = counter
            counter = counter + 1

prob_mat = np.zeros((counter, counter), dtype=float)
transient = []
absorbing = []
mine = []
exit_ = []
blocked = []
starting_point = 0
for row in range(n):
    for col in range(m):
        if (matrix[row][col] == OBSTACLE):
            continue
        elif ((matrix[row][col] == START) or (matrix[row][col] == FREE) or
                (matrix[row][col] == TUNNEL)):
            if (am_I_stuck(row, col)):
                blocked.append(index(row, col))
                prob_mat[index(row, col)][index(row, col)] = 1
                continue
            transient.append(index(row, col))
            if (matrix[row][col] == START):
                starting_point = len(transient) - 1
            for key, val in calc_prob(row, col).items():
                prob_mat[index(row, col)][key] = val
                # print("row:"+str(row)+"key:"+str(key)+"val:"+str(val))
        elif matrix[row][col] == MINE:
            prob_mat[index(row, col)][index(row, col)] = 1
            mine.append(index(row, col))
        elif matrix[row][col] == EXIT:
            prob_mat[index(row, col)][index(row, col)] = 1
            exit_.append(index(row, col))

absorbing = mine + exit_ + blocked
print("Matrix:" + str(matrix))
print("Probability Matrix:")
print(str(prob_mat))
np.savetxt("prob_mat.csv", prob_mat, delimiter=",", fmt=out_format)
Q = copy.deepcopy(prob_mat)
R = copy.deepcopy(prob_mat)
transient.sort(reverse=True)
for count in sorted(absorbing, reverse=True):
    Q = np.delete(Q, count, axis=0)
    Q = np.delete(Q, count, axis=1)
    R = np.delete(R, count, axis=0)
for count in transient:
    R = np.delete(R, count, axis=1)
print("Transient Matrix:")
print(str(Q))
np.savetxt("transient.csv", Q, delimiter=",", fmt=out_format)
print("Absorbant Matrix:")
print(str(R))
np.savetxt("absorbant.csv", R, delimiter=",", fmt=out_format)
N = np.identity(Q.shape[0]) - Q
print("Resultant N:" + str(N))
print("shape:" + str(N.shape) + ", dtype:" + str(N.dtype))
print("Determinant of Q:" + str(np.linalg.det(Q)))
print("Determinant of N:" + str(np.linalg.det(N)))
N = np.linalg.inv(N)
print("Inverse:")
print(str(N))
np.savetxt("inverse.csv", N, delimiter=",", fmt=out_format)
B = N.dot(R)
print("Result:")
print(str(B))
np.savetxt("result.csv", B, delimiter=",", fmt=out_format)
prob = 0.0
for i in exit_:
    pos = absorbing.index(i)
    prob = prob + B[starting_point][pos]
print("Final Probability:" + str(prob))
