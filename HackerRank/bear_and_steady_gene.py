#!/bin/python3

import sys


def validityCheck(dic, limit):
    if(dic['A'] <= limit and dic['C'] <= limit and dic['G'] <= limit and dic['T'] <= limit):
        return True
    else:
        return False


def steadyGene(gene):
    global N
    dic = {'A': 0, 'G': 0, 'C': 0, 'T': 0}
    limit = int(N / 4)
    out = sys.maxsize
    maxIndex = 0

    for i in reversed(range(N)):
        dic[gene[i]] += 1
        if not validityCheck(dic, limit):
            maxIndex = i + 1
            dic[gene[i]] -= 1
            break

    minIndex = -1
    while minIndex < N - 1 and minIndex < maxIndex:

        while (not validityCheck(dic, limit) and (maxIndex < N)):
            dic[gene[maxIndex]] -= 1
            maxIndex += 1

        if((maxIndex > N) or (not validityCheck(dic, limit))):
            break

        substringLength = max(0, maxIndex - minIndex - 1)
        if substringLength < out:
            out = substringLength

        dic[gene[minIndex + 1]] += 1
        minIndex += 1

    return out


if __name__ == '__main__':
    N = int(input())
    gene = input()
    result = steadyGene(gene)
    print(str(result))
