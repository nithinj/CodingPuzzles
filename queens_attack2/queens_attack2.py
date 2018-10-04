def left(row, col):
    global mat

    if (row < 0) or (row * n + col in mat):
        return 0
    return 1 + left(row - 1, col)


def right(row, col):
    global mat

    if (row > n - 1) or (row * n + col in mat):
        return 0
    return 1 + right(row + 1, col)


def top(row, col):
    global mat

    if (col > n - 1) or (row * n + col in mat):
        return 0
    return 1 + top(row, col + 1)


def bottom(row, col):
    global mat

    if (col < 0) or (row * n + col in mat):
        return 0
    return 1 + bottom(row, col - 1)


def topleft(row, col):
    global mat

    if (row < 0) or (col > n - 1) or (row * n + col in mat):
        return 0
    return 1 + topleft(row - 1, col + 1)


def bottomleft(row, col):
    global mat

    if (row < 0) or (col < 0) or (row * n + col in mat):
        return 0
    return 1 + bottomleft(row - 1, col - 1)


def topright(row, col):
    global mat

    if (row > n - 1) or (col > n - 1) or (row * n + col in mat):
        return 0
    return 1 + topright(row + 1, col + 1)


def bottomright(row, col):
    global mat

    if (row > n - 1) or (col < 0) or (row * n + col in mat):
        return 0
    return 1 + bottomright(row + 1, col - 1)


def queens_attack():
    global mat, queen
    count = 0

    count += left(queen[0] - 1, queen[1])
    count += right(queen[0] + 1, queen[1])
    count += top(queen[0], queen[1] + 1)
    count += bottom(queen[0], queen[1] - 1)
    count += topright(queen[0] + 1, queen[1] + 1)
    count += topleft(queen[0] - 1, queen[1] + 1)
    count += bottomleft(queen[0] - 1, queen[1] - 1)
    count += bottomright(queen[0] + 1, queen[1] - 1)

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
