from sys import stdin


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