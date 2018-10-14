#!/bin/python3
from copy import deepcopy


class Node():

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.val = 1
        self.possess = {}


def twoPluses(grid):
    global n, m

    candidates = []
    atleast_one = 0

    for i in range(1, n - 1):
        for j in range(1, m - 1):
            if grid[i][j] == 'G':
                atleast_one = 1
                ll = [i * m + j]
                inc = 1
                first = 1
                while True:
                    count = 0
                    if i + inc < n and grid[i + inc][j] == 'G':
                        count += 1
                        ll.append((i + inc) * m + j)
                    if i - inc >= 0 and grid[i - inc][j] == 'G':
                        count += 1
                        ll.append((i - inc) * m + j)
                    if j + inc < m and grid[i][j + inc] == 'G':
                        count += 1
                        ll.append(i * m + j + inc)
                    if j - inc >= 0 and grid[i][j - inc] == 'G':
                        count += 1
                        ll.append(i * m + j - inc)
                    if count < 4:
                        break
                    if first:
                        node = Node(i, j)
                        candidates.append(node)
                        first = 0
                    node.val += count
                    node.possess[node.val] = deepcopy(ll)
                    inc += 1

    if len(candidates) == 0:
        if atleast_one:
            return 1
        else:
            return 0
    if len(candidates) == 1:
        return candidates[0].val

    candidates.sort(key=lambda x: x.val, reverse=True)

    res = [5]
    for i in range(len(candidates) - 1):
        for j in range(i, len(candidates)):
            count = 5
            if not (set(candidates[i].possess[count]) & set(candidates[j].possess[count])):
                last = 25
                while count <= candidates[i].val:
                    count2 = 5
                    failed = 0
                    while count2 <= count and count2 <= candidates[j].val:
                        if not (set(candidates[i].possess[count]) & set(candidates[j].possess[count2])):
                            if (count * count2 > last):
                                last = count * count2
                            count2 += 4
                        else:
                            failed = 1
                            break
                    if not failed:
                        count += 4
                    else:
                        break
                res.append(last)
    return max(res)


if __name__ == '__main__':
    nm = input().split()
    n = int(nm[0])
    m = int(nm[1])
    grid = []
    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)
    result = twoPluses(grid)
    print(str(result))
