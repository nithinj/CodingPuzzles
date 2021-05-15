#!/bin/python3

(unvisited, partial, visited) = (0, 1, 2)


class Node():
    def __init__(self, name):
            self.id = name
            self.adj = []
            self.visited = unvisited


def has_cycle(root):
    if not root:
        return False

    #print("node=" + str(root.id) + "; visited=" + str(root.visited) + "; adj=" + str(root.adj))

    if root.visited == partial:
        return True

    if root.visited == visited:
        return False

    root.visited = partial

    cycle_found = False
    num_visits = 0
    for v in root.adj:
        cycle_found = has_cycle(graph[v])
        if graph[v].visited == visited:
            num_visits += 1

    if num_visits == len(root.adj):
        root.visited = visited

    return cycle_found

if __name__ == '__main__':

    N,E = map(int, input().split(','))
    graph = {}
    for pair in input().split(','):
        (k, v) = pair.split('->')
        if k in graph:
            graph[v] = Node(v)
            graph[k].adj.append(v)
        else:
            graph[k] = Node(v)

    cycle_found = False
    for val in graph.values():
        if has_cycle(val):
            cycle_found = True
    if cycle_found:
        print("Yes")
    else:
        print("No")
