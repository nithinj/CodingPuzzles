#!/bin/python3


def matchingStrings(strings, queries):
    dic = {}
    for string in strings:
        if string in dic:
            dic[string] += 1
        else:
            dic[string] = 1
    res = []
    for query in queries:
        if query in dic:
            res.append(dic[query])
        else:
            res.append(0)
    return res

if __name__ == '__main__':
    strings_count = int(input())
    strings = []
    for _ in range(strings_count):
        strings_item = input()
        strings.append(strings_item)
    queries_count = int(input())
    queries = []
    for _ in range(queries_count):
        queries_item = input()
        queries.append(queries_item)
    res = matchingStrings(strings, queries)
    print('\n'.join(map(str, res)))
