#!/bin/python3


def sherlockAndAnagrams(s):
    substr = []
    for i in range(len(s)):
        substr.append([])
        j = 0
        while j + i < len(s):
            substr[i].append(sorted(s[j: j + i + 1]))
            j += 1
    count = 0
    for sublist in substr:
        for i in range(len(sublist)):
            for j in range(i + 1, len(sublist)):
                if sublist[j] == sublist[i]:
                    count += 1
    return count


if __name__ == '__main__':
    q = int(input())
    for q_itr in range(q):
        s = input()
        result = sherlockAndAnagrams(s)
        print(str(result))
