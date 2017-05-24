from sys import stdin
import math


def calc_modulo(n):
    exp = 0
    for i in range(calc_modulo.starting_count, n + 1):
        if calc_modulo.starting_count == 0 and (1 << i) > mod_const:
            calc_modulo.starting_count = i
        if exp == 0:
            exp = (1 << i) % mod_const
        else:
            exp = (exp * 2) % mod_const
    return int(exp)


inp = []
mod_const = int(math.pow(10, 9) + 7)
calc_modulo.starting_count = 0
n = int(stdin.readline())
for i in range(n):
    m = int(stdin.readline())
    inp = stdin.readline().split()
    inp = [int(x) for x in inp]
    res = 0
    for i in range(len(inp)):
        res = res | inp[i]
    res = int(res % mod_const)
    res = res * calc_modulo(m - 1)
    print(str(int(res % mod_const)))
