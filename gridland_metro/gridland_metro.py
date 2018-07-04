from sys import stdin


inp = stdin.readline().split()
inp = [int(x) for x in inp]
(n, m, k) = (inp[0], inp[1], inp[2])
mat = []
for i in range(n):
    mat.append([1] * m)
for i in range(k):
    inp = stdin.readline().split()
    inp = [int(x) for x in inp]
    for j in range(inp[1] - 1, inp[2]):
        mat[inp[0] - 1][j] = 0
#print("Matrix:")
#print(str(mat))
tot = 0
for i in range(n):
    tot += sum(mat[i])
print(str(tot))
