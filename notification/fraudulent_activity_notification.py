#!/bin/python3

import math
import os
import random
import re
import sys


def activityNotifications(expenditure, d):
    notification = 0
    sorted_ = 0
    exp_list = []
    for i in range(d, len(expenditure)):
        if sorted_ == 0:
            exp_list = expenditure[i - d: i]
            exp_list.sort()
            sorted_ = 1
        else:
            exp_list.remove(expenditure[i - d])
            next_ = expenditure[i - 1]
            (low, high) = (0, len(exp_list))
            while(low <= high):
                mid = int((low + high) / 2)
                elm = exp_list[mid]
                if (mid == 0 and elm > next_) or (mid == len(exp_list) - 1 and elm < next_):
                    exp_list.insert(mid, next_)
                    break
                elif (next_ >= exp_list[mid - 1] and next_ <= exp_list[mid]):
                    exp_list.insert(mid, next_)
                    break
                if next_ > elm:
                    low = mid
                else:
                    high = mid

        if (d % 2 == 0):
            med = exp_list[int(d / 2)] + exp_list[int(d / 2) - 1]
        else:
            med = exp_list[int(d / 2)]
        if expenditure[i] >= med * 2:
            notification += 1

    return notification


nd = input().split()

n = int(nd[0])

d = int(nd[1])

expenditure = list(map(int, input().rstrip().split()))

result = activityNotifications(expenditure, d)

print(str(result) + '\n')
