#!/bin/python3

import sys
from queue import Queue


sys.setrecursionlimit(2048)
COUNT = 10


class Node:

    def __init__(self, val, depth):
        self.val = val
        self.depth = depth
        self.left = None
        self.right = None

    def __repr__(self):
        return ("val:" + str(self.val) + " depth:" + str(self.depth) +
                " left:" + str(self.left) + " right:" + str(self.right))


def print_inorder(root, res):
    if (root):
        print_inorder(root.left, res)
        res.append(root.val)
        print_inorder(root.right, res)


def swapNodes(indexes, queries):
    que = Queue()
    dic = {}

    root = Node(1, 1)
    dic[1] = [root]
    que.put(root)

    for item in indexes:
        node = que.get()
        if item[0] != -1:
            left = Node(item[0], node.depth + 1)
            node.left = left
            que.put(left)
            if left.depth in dic:
                dic[left.depth].append(left)
            else:
                dic[left.depth] = [left]
        if item[1] != -1:
            right = Node(item[1], node.depth + 1)
            node.right = right
            que.put(right)
            if right.depth in dic:
                dic[right.depth].append(right)
            else:
                dic[right.depth] = [right]

    out = []
    for k in queries:
        k_orig = k
        while k in dic:
            for node in dic[k]:
                node.left, node.right = node.right, node.left
            k += k_orig
        res = []
        print_inorder(root, res)
        out.append(res)
    return out


if __name__ == '__main__':
    n = int(input())
    indexes = []
    for _ in range(n):
        indexes.append(list(map(int, input().rstrip().split())))
    queries_count = int(input())
    queries = []
    for _ in range(queries_count):
        queries_item = int(input())
        queries.append(queries_item)
    result = swapNodes(indexes, queries)
    print('\n'.join([' '.join(map(str, x)) for x in result]))
