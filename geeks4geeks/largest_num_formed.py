"""
Given an array of numbers, arrange them in a way that yields the largest value.
For example, if the given numbers are {54, 546, 548, 60}, the arrangement 6054854654 gives the largest value.
And if the given numbers are {1, 34, 3, 98, 9, 76, 45, 4}, then the arrangement 998764543431 gives the largest value.
"""

from functools import cmp_to_key

def compare(x, y):
        xy = str(x) + str(y)
        yx = str(y) + str(x)
        return int(xy) - int(yx)


def largest(arr):
        arr = sorted(arr, key = cmp_to_key(compare))
        #print(str(arr))
        out = ''
        for num in arr[::-1]:
                out += str(num)
        print(out)
        return int(out)

def test():
        assert(largest([54, 546, 548, 60]) == 6054854654)
        assert(largest([1, 34, 3, 98, 9, 76, 45, 4]) == 998764543431)

test()
        

