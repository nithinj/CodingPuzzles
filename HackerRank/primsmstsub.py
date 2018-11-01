#!/bin/python3

from queue import PriorityQueue


def prims(n, edges, start):
    graph = {}

    for edge in edges:
        if edge[0] in graph:
            graph[edge[0]].append((edge[1], edge[2]))
        else:
            graph[edge[0]] = [(edge[1], edge[2])]
        if edge[1] in graph:
            graph[edge[1]].append((edge[0], edge[2]))
        else:
            graph[edge[1]] = [(edge[0], edge[2])]

    unvisited = [x for x in range(1, n + 1)]
    visited = [start]
    del unvisited[start - 1]
    min_cost = 0
    q = PriorityQueue()

    while unvisited:
        for dest, dist in graph[visited[-1]]:
            if dest not in visited:
                q.put((dist, dest))
        min_elem = q.get()
        while min_elem[1] in visited:
            min_elem = q.get()
        visited.append(min_elem[1])
        unvisited.remove(min_elem[1])
        min_cost += min_elem[0]

    return min_cost


if __name__ == '__main__':
    nm = input().split()
    n = int(nm[0])
    m = int(nm[1])
    edges = []
    for _ in range(m):
        edges.append(list(map(int, input().rstrip().split())))
    start = int(input())

    result = prims(n, edges, start)
    print(str(result))
