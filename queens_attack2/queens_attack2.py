
def queens_attack():
    global mat, queen
    count = 0

    [row, col] = queen
    row -= 1
    while (row >= 0) and (row * n + col not in mat):
        count += 1
        row -= 1

    [row, col] = queen
    row += 1
    while (row < n) and (row * n + col not in mat):
        count += 1
        row += 1

    [row, col] = queen
    col += 1
    while (col < n) and (row * n + col not in mat):
        count += 1
        col += 1

    [row, col] = queen
    col -= 1
    while (col >= 0) and (row * n + col not in mat):
        count += 1
        col -= 1

    [row, col] = queen
    row -= 1
    col += 1
    while (row >= 0) and (col < n) and (row * n + col not in mat):
        count += 1
        row -= 1
        col += 1

    [row, col] = queen
    row -= 1
    col -= 1
    while (row >= 0) and (col >= 0) and (row * n + col not in mat):
        count += 1
        row -= 1
        col -= 1

    [row, col] = queen
    row += 1
    col += 1
    while (row < n) and (col < n) and (row * n + col not in mat):
        count += 1
        row += 1
        col += 1

    [row, col] = queen
    row += 1
    col -= 1
    while (row < n) and (col >= 0) and (row * n + col not in mat):
        count += 1
        row += 1
        col -= 1

    return count


nk = input().split()
n = int(nk[0])
k = int(nk[1])
mat = {}

queen = [int(x) - 1 for x in input().rstrip().split()]
for i in range(k):
    [r, c] = [int(x) - 1 for x in input().rstrip().split()]
    mat[r * n + c] = 1

pos = queens_attack()
print(str(pos))
