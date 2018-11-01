#!/bin/python3


def calc(node):
    sum = 0
    for child in node:
        if child in evenForest.tree:
            sum += calc(evenForest.tree[child])
        else:
            sum += 1
    if ((sum + 1) % 2 == 0):
        evenForest.res += 1
        return 0
    else:
        return sum + 1


def evenForest(t_nodes, t_edges, t_from, t_to):
    evenForest.tree = {}
    for i in range(t_edges):
        if t_from[i] < t_to[i]:
            from_, to = t_from[i], t_to[i]
        else:
            from_, to = t_to[i], t_from[i]
        if from_ in evenForest.tree:
            evenForest.tree[from_].append(to)
        else:
            evenForest.tree[from_] = [to]
    evenForest.res = 0
    calc(evenForest.tree[1])
    return evenForest.res

if __name__ == '__main__':
    t_nodes, t_edges = map(int, input().rstrip().split())
    t_from = [0] * t_edges
    t_to = [0] * t_edges
    for i in range(t_edges):
        t_from[i], t_to[i] = map(int, input().rstrip().split())
    res = evenForest(t_nodes, t_edges, t_from, t_to)
    print(str(res - 1))
