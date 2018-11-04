#!/bin/python3

import sys
import time


def shortestPath(V, E, edge_from, edge_to, weight):
    dist = []
    for i in range(V):
        dist.append([sys.maxsize] * V)
    for i in range(E):
        dist[edge_from[i] - 1][edge_to[i] - 1] = weight[i]
    for i in range(V):
        dist[i][i] = 0

    start = time.time()
    for k in range(V):
        for i in range(V):
            for j in range(V):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    print("time:" + str(time.time() - start))
    return dist


if __name__ == '__main__':
    road_nodes, road_edges = map(int, input().split())

    road_from = [0] * road_edges
    road_to = [0] * road_edges
    road_weight = [0] * road_edges

    for i in range(road_edges):
        road_from[i], road_to[i], road_weight[i] = map(int, input().split())

    dist = shortestPath(road_nodes, road_edges,
                        road_from, road_to, road_weight)

    q = int(input())

    for q_itr in range(q):
        x, y = map(int, input().split())
        d = dist[x - 1][y - 1]
        if d == sys.maxsize:
            print(-1)
        else:
            print(str(d))
