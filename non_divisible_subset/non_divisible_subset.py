#!/bin/python3


def nonDivisibleSubset(k, S):
	list_of_sets = []
    for i in range(len(S)):
        for j in range(i + 1, len(S)):
        	found = 0
            if ((S[i] + S[j]) % k == 0):
            	for elm in list_of_sets:
            		if (S[i] in elm):
            			found = 1
            			candidate = 1
            			for num in (elm - set(S[i]):
            				if (num + S[i]) % k != 0:
            					candidate = 0
            					break
            			if candidate:
        					elm.add(S[i])
        			if (S[j] in elm):
            			found = 1
            			candidate = 1
            			for num in (elm - set(S[j]):
            				if (num + S[j]) % k != 0:
            					candidate = 0
            					break
            			if candidate:
        					elm.add(S[i])
        		if not found:
        			list_of_sets.append(set([S[i], S[j]]))

    return max(list_of_sets, key=lambda arg:len(arg))




nk = input().split()

n = int(nk[0])

k = int(nk[1])

S = list(map(int, input().rstrip().split()))

result = nonDivisibleSubset(k, S)

print(str(result))
