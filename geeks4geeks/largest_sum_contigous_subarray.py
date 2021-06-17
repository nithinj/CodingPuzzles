import sys

def sum(arr):
        max_so_far = -sys.maxint - 1
        current_sum = 0
        for num in arr:
                current_sum += num
                if max_so_far < current_sum:
                        max_so_far = current_sum
                if current_sum < 0:
                        current_sum = 0

        return max_so_far


def test1(): # sum is 7
        print(str(sum([-1, -3, 4, -1, -2, 1, 5, -3])))

test1()