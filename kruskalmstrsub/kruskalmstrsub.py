#!/bin/python3

# The function is expected to return an INTEGER.
# The function accepts WEIGHTED_INTEGER_GRAPH g as parameter.
#

#
# For the weighted graph, <name>:
#
# 1. The number of nodes is <name>_nodes.
# 2. The number of edges is <name>_edges.
# 3. An edge exists between <name>_from[i] and <name>_to[i]. The weight of the edge is <name>_weight[i].
#
#


def kruskals(g_nodes, g_from, g_to, g_weight):
    global g_edges

    graph = []
    for i in range(g_edges):
        graph.append([g_from[i], g_to[i], g_weight[i]])
    graph.sort(key=lambda x: x[2])
    # print(str(graph))
    visited = set()
    list_of_sets = []
    tot = 0
    for item in graph:
        circle = 0
        s1, s2 = -1, -1
        max_len = 0
        updated = 0
        if (item[0] in visited) or (item[1] in visited):
            for i in range(len(list_of_sets)):
                if len(list_of_sets[i]) > max_len:
                    max_len = len(list_of_sets[i])
                if item[0] in list_of_sets[i]:
                    s1 = i
                if item[1] in list_of_sets[i]:
                    s2 = i
            #print("s1:" + str(s1) + "s2:" + str(s2))
            if s1 != -1 and s1 == s2:
                circle = 1
            elif s1 != -1 and s2 == -1:
                list_of_sets[s1].update(item[0:2])
                if len(list_of_sets[s1]) > max_len:
                    max_len = len(list_of_sets[s1])
                updated = 1
            elif s2 != -1 and s1 == -1:
                list_of_sets[s2].update(item[0:2])
                if len(list_of_sets[s2]) > max_len:
                    max_len = len(list_of_sets[s2])
                updated = 1
            elif s1 != -1 and s2 != -1:
                list_of_sets[s1].update(list_of_sets[s2])
                if len(list_of_sets[s1]) > max_len:
                    max_len = len(list_of_sets[s1])
                del list_of_sets[s2]
                updated = 1
            else:
                list_of_sets.append(set(item[0:2]))
                updated = 1

        if not circle:
            tot += item[2]
            visited.update(item[0:2])
            if not updated:
                list_of_sets.append(set(item[0:2]))
        # print("item:" + str(item) + " tot:" + str(tot) + " visited:" + str(visited) + " circle:" +
         # str(circle) + " max_len:" + str(max_len) + " list_of_sets:" +
         # str(list_of_sets))
        if max_len == g_nodes:
            return tot


if __name__ == '__main__':
    g_nodes, g_edges = map(int, input().rstrip().split())
    g_from = [0] * g_edges
    g_to = [0] * g_edges
    g_weight = [0] * g_edges
    for i in range(g_edges):
        g_from[i], g_to[i], g_weight[i] = map(int, input().rstrip().split())
    res = kruskals(g_nodes, g_from, g_to, g_weight)
    print(str(res))
