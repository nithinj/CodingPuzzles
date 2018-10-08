#!/bin/python3


def gridSearch(G, P):
    for i in range(len(G)):
        if P[0] in G[i]:
            found = 1
            indices = []
            ind = -1
            while True:
                ind = G[i].find(P[0], ind + 1)
                if ind == -1:
                    break
                indices.append(ind)
            for j in range(1, len(P)):
                if (i + j >= len(G)) or (G[i + j].find(P[j]) not in indices):
                    found = 0
                    break
            if found:
                return "YES"
    return "NO"


if __name__ == '__main__':

    t = int(input())
    for t_itr in range(t):
        RC = input().split()
        R = int(RC[0])
        C = int(RC[1])
        G = []
        for _ in range(R):
            G_item = input()
            G.append(G_item)
        rc = input().split()
        r = int(rc[0])
        c = int(rc[1])
        P = []
        for _ in range(r):
            P_item = input()
            P.append(P_item)
        result = gridSearch(G, P)
        print(result)
