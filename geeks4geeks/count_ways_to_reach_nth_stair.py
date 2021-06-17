
def count_ways(n, m):
        res = [1]
        temp = 0
        for i in range(1, n + 1):
                start = i - m - 1
                if start >=0:
                        temp -= res[start]
                temp += res[-1]
                res.append(temp)

        print(str(res[-1]))
        return res[-1]


def test1():
        return count_ways(5, 2)
def test2():
        return count_ways(1, 2)
def test3():
        return count_ways(2, 2)
def test4():
        return count_ways(4, 2)
def test5():
        return count_ways(5, 3)

# Invoke test funtions
if test1() == 8:
        print("Test1 passed")
if test2() == 1:
        print("Test2 passed")
if test3() == 2:
        print("Test3 passed")
if test4() == 5:
        print("Test4 passed")
if test5() == 13:
        print("Test5 passed")
