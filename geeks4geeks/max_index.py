import sys

# For a given array inp[],
# returns the maximum j - i
# such that inp[j] > inp[i]
def MaxIndex(inp, N):
    LMin = [inp[0]] * N
    RMax = [inp[-1]] * N

    for i in range(N - 2, -1, -1):
        RMax[i] = max(RMax[i + 1], inp[i])

    for i in range(1, N):
        LMin[i] = min(LMin[i - 1], inp[i])

    MaxDiff = -1
    i, j = 0, 0
    while ((i < N) and (j < N)):
        if LMin[i] < RMax[j]:
            MaxDiff = max(MaxDiff, j - i)
            j += 1
        else:
            i += 1

    return MaxDiff


def test1(): # result = 6
    a = [34, 8, 10, 3, 2, 80, 30, 33, 1]
    print(str(MaxIndex(a, len(a))))

def test2(): # result = 8
    a = [9, 2, 3, 4, 5, 6, 7, 8, 18, 0]
    print(str(MaxIndex(a, len(a))))

def test3(): # result = 5
    a = [1, 2, 3, 4, 5, 6]
    print(str(MaxIndex(a, len(a))))

def test4(): # result = -1
    a = [6, 5, 4, 3, 2, 1]
    print(str(MaxIndex(a, len(a))))

def test5(): # result = 7
    a = [7, 3, 1, 8, 9, 10, 4, 5, 6]
    print(str(MaxIndex(a, len(a))))

test1()
test2()
test3()
test4()
test5()