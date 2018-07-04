from sys import stdin


inp = stdin.readline().split()
inp = [int(x) for x in inp]
(n, m, k) = (inp[0], inp[1], inp[2])
mat = {}
for i in range(k):
    inp = stdin.readline().split()
    inp = [int(x) for x in inp]
    if inp[0] in mat:
        for item in mat[inp[0]]:
            if (((inp[1] >= item[0]) and (inp[1] <= item[1])) or
                    ((inp[2] >= item[0]) and (inp[2] <= item[1]))):
                if (inp[1] < item[0]):
                    item[0] = inp[1]
                if (inp[2] > item[1]):
                    item[1] = inp[2]
            else:
                mat[inp[0]].append(inp[1:])
    else:
        mat[inp[0]] = [inp[1:]]
tot = 0
for val in mat.itervalues():
    for item in val:
        tot += item[1] - item[0] + 1
print(str((n * m) - tot))
