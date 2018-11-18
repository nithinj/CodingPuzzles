#!/bin/python3

from collections import Counter


def Parent(x):
    global parents

    if parents[x] != x:
        parents[x] = Parent(parents[x])
    return parents[x]


def componentsInGraph(gb, n):
    global parents

    for item in gb:
        p1, p2 = Parent(item[0]), Parent(item[1])
        parents[item[0]] = parents[item[1]] = parents[
            p1] = parents[p2] = min(p1, p2)

    # resolve anomolies
    for i in range(2 * n + 1):
        par = Parent(i)
        parents[i] = par

    count = Counter()
    for p in parents:
        count[p] += 1
    res = [x for x in count.values() if x > 1]
    return [min(res), max(res)]


if __name__ == '__main__':
    n = int(input())
    gb = []
    parents = list(range(2 * n + 1))

    for _ in range(n):
        gb.append(list(map(int, input().rstrip().split())))

    result = componentsInGraph(gb, n)
    print(' '.join(map(str, result)))
