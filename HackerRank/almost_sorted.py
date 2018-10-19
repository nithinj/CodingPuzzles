#!/bin/python3


def almostSorted(arr):
    sorted_arr = sorted(arr)
    (start, end, count) = (-1, -1, 0)
    for i in range(len(sorted_arr)):
        if sorted_arr[i] != arr[i]:
            if start == -1:
                start = i
            else:
                end = i
            count += 1
    if count == 2:
        print("yes\nswap " + str(start + 1) + " " + str(end + 1))
    elif count > 2:
        dup_arr = arr[: start] + arr[end: start - 1: -1] + arr[end + 1:]
        if dup_arr == sorted_arr:
            print("yes\nreverse " + str(start + 1) + " " + str(end + 1))
        else:
            print("no")
    else:
        print("no")


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    almostSorted(arr)
