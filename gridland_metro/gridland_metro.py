from sys import stdin


inp = stdin.readline().split()
inp = [int(x) for x in inp]
(n, m, k) = (inp[0], inp[1], inp[2])
mat = {}
for i in range(k):
    inp = stdin.readline().split()
    inp = [int(x) for x in inp]
    if inp[0] in mat:
        if (inp[1] < mat[inp[0]][0]):
            mat[inp[0]][0] = inp[1]
        if (inp[2] > mat[inp[0]][1]):
            mat[inp[0]][1] = inp[2]
    else:
        mat[inp[0]] = inp[1:]
tot = 0
for val in mat.itervalues():
    tot += val[1] - val[0] + 1
print(str((n * m) - tot))
