#!/bin/python3


def truckTour(petrolpumps, n):
    rem = 0

    for start in range(n):
        i = rem = 0
        while rem >= 0:
            ind = (start + i) % n
            rem += petrolpumps[ind][0] - petrolpumps[ind][1]
            i += 1
            if (i == n - 1) and rem >= 0:
                return start

if __name__ == '__main__':
    n = int(input())
    petrolpumps = []

    for _ in range(n):
        petrolpumps.append(list(map(int, input().rstrip().split())))

    result = truckTour(petrolpumps, n)
    print(str(result))
