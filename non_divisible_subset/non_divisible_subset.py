#!/bin/python3

DBG = 1


def nonDivisibleSubset(k, S):
    list_of_sets = []
    for i in range(len(S)):
        for j in range(i + 1, len(S)):
            found = 0
            if DBG:
                print("S[i]: " + str(S[i]) + " S[j]: " + str(S[j]))
            if ((S[i] + S[j]) % k != 0):
                for elm in list_of_sets:
                    if (S[i] in elm):
                        found = 1
                        candidate = 1
                        for num in (elm - {S[i]}):
                            if ((num + S[j]) % k) == 0:
                                candidate = 0
                                break
                        if candidate:
                            if DBG:
                                print(str(elm) + ", adding:" + str(S[j]))
                            elm.add(S[j])
                    if (S[j] in elm):
                        found = 1
                        candidate = 1
                        for num in (elm - {S[j]}):
                            if ((num + S[i]) % k) == 0:
                                candidate = 0
                                break
                        if candidate:
                            if DBG:
                                print(str(elm) + ", adding:" + str(S[i]))
                            elm.add(S[i])
                if not found:
                    if ((S[i] + S[j]) % k) != 0:
                        list_of_sets.append(set([S[i], S[j]]))
                    else:
                        list_of_sets.append({S[i]})
                        list_of_sets.append({S[j]})

    if DBG:
        max(list_of_sets, key=lambda arg: len(arg))
    return len(max(list_of_sets, key=lambda arg: len(arg)))


nk = input().split()

n = int(nk[0])

k = int(nk[1])

S = list(map(int, input().rstrip().split()))

result = nonDivisibleSubset(k, S)

print(str(result))
