#!/bin/python3


def convert(x):
    return {
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine",
        10: "ten",
        11: "eleven",
        12: "twelve",
        13: "thirteen",
        14: "forteen",
        15: "fifteen",
        16: "sixteen",
        17: "seventeen",
        18: "eighteen",
        19: "ninteen",
        20: "twenty"
    }.get(x, 0)


def timeInWords(h, m):
    res = ""
    if m == 0:
        res = convert(h) + " o' clock"
        return res
    if m > 30:
        m = 60 - m
        h += 1
        res += "to " + convert(h)
    else:
        res += "past " + convert(h)
    if m == 15:
        res = "quarter " + res
    elif m == 30:
        res = "half " + res
    elif m < 21:
        if m == 1:
            res = convert(m) + " minute " + res
        else:
            res = convert(m) + " minutes " + res
    else:
        res = "twenty " + convert(m - 20) + " minutes " + res

    return res


if __name__ == '__main__':

    h = int(input())
    m = int(input())
    result = timeInWords(h, m)
    print(result)
