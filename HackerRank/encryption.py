import math


def encryption(s):
    newstr = s.replace(" ", "")
    n = math.ceil(len(newstr)**(1 / 2))
    res = []

    for i in range(n):
        j = i
        while j < len(newstr):
            res.append(newstr[j])
            j += n
        res.append(' ')
    return ''.join(res)


if __name__ == '__main__':

    s = input()
    result = encryption(s)
    print(result)
