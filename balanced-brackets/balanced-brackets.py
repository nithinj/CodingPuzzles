#!/bin/python3


def isBalanced(s):
    opening = ['(', '[', '{']
    closing = [')', ']', '}']
    stack = []

    for letter in s:
        if letter in opening:
            stack.append(letter)
        elif letter in closing:
            if (not stack) or (stack.pop() != opening[closing.index(letter)]):
                return "NO"
    if not stack:
        return "YES"
    else:
        return "NO"


if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)
        print(result)
