from sys import stdin
import math

divisor = math.pow(10, 9) + 7

n = int(stdin.readline())
for i in range(n):
    inp = stdin.readline().split()
    inp = [int(x) for x in inp]
    m = inp[0]
    n = inp[1]
    row = stdin.readline().split()
    row = [int(x) for x in row]
    col = stdin.readline().split()
    col = [int(x) for x in col]
    row.sort(reverse=True)
    col.sort(reverse=True)
    (j, k, x, y, min_cost) = [0] * 5
    while ((j < len(row)) or (k < len(col))):
        if (j >= len(row)):
            min_cost = min_cost + (col[k] * (x + 1))
            k = k + 1
            y = y + 1
        elif (k >= len(col)):
            min_cost = min_cost + (row[j] * (y + 1))
            j = j + 1
            x = x + 1
        elif (row[j] < col[k]):
            min_cost = min_cost + (col[k] * (x + 1))
            k = k + 1
            y = y + 1
        elif (row[j] >= col[k]):
            min_cost = min_cost + (row[j] * (y + 1))
            j = j + 1
            x = x + 1
        else:
            print("I'm doing something stupid!")
        if min_cost > divisor:
            min_cost = min_cost % divisor
    print(str(int(min_cost)))
