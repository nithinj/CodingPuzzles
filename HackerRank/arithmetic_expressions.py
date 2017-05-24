import fileinput
from sys import stdin
from math import ceil


def easy_way():
    global a, op, flag, n
    res = a[0]
    for i in range(1, n):
        res += a[i]
        op[i - 1] = '+'
        if (res % 101 == 0):
            i = i + 1
            while(i != n):
                op[i - 1] = '*'
                i = i + 1
            return 1

    res = a[0]
    for i in range(1, n):
        res -= a[i]
        op[i - 1] = '-'
        if (res % 101 == 0):
            i = i + 1
            while(i != n):
                op[i - 1] = '*'
                i = i + 1
            return 1

    return 0


def calculate(ind, res):
    global a, op, flag, n, bucket
    if (res % 101 == 0):
        while(ind != n):
            op[ind - 1] = '*'
            ind = ind + 1
        flag = 1
        return

    if (flag == 1 or ind >= n):
        return

    if(((res + a[ind]) % 101) < ((res - a[ind]) % 101)):
        op[ind - 1] = '+'
        calculate(ind + 1, res + a[ind])

        if (flag == 1 or ind >= n):
            return
        op[ind - 1] = '-'
        calculate(ind + 1, res - a[ind])
    else:
        if (flag == 1 or ind >= n):
            return
        op[ind - 1] = '-'
        calculate(ind + 1, res - a[ind])

        if (flag == 1 or ind >= n):
            return
        op[ind - 1] = '+'
        calculate(ind + 1, res + a[ind])

    if (flag == 1 or ind >= n or bucket):
        return
    op[ind - 1] = '*'
    calculate(ind + 1, res * a[ind])


def bucket_way():
    global a, op, flag, n, bucket
    d = {}
    for num in a:
        if num in d:
            d[num] = d[num] + 1
        else:
            d[num] = 1

    if len(d) <= ceil(n / 10):
        temp_inp = a.copy()
        temp_n = n
        a = []
        k = []
        for key, value in d.items():
            if key == temp_inp[0]:
                a.insert(0, key * value)
                k.insert(0, key)
            else:
                a.append(key * value)
                k.append(key)
        n = len(a)
        bucket = 1
        calculate(1, a[0])
        bucket = 0
        if flag == 1:
            op.insert(0, '+')
            temp_op = op.copy()
            for i in range(1, temp_n):
                op[i - 1] = temp_op[k.index(temp_inp[i])]
        a = temp_inp
        n = temp_n
        return flag
    return 0


(flag, bucket) = (0, 0)
n = int(stdin.readline())
op = [None] * (n - 1)
a = list()
sum = 0

for i in stdin.readline().split():
    a.append(int(i))
    sum += int(i)

if (not easy_way()) and (not bucket_way()):
    calculate(1, a[0])

out = str()
for i in range(n - 1):
    out += str(a[i]) + str(op[i])
out += str(a[n - 1])
print(out)
