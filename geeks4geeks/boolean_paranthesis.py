from copy import deepcopy

def form_expr(symbol, oper):
        for i in range(len(symbol)):
                if symbol[i] == 'T':
                        symbol[i] = '1'
                elif symbol[i] == 'F':
                        symbol[i] = '0'
        for i in range(len(oper)):
                symbol.insert(i * 2 + 1, oper[i])
        return symbol

matched = []
def countways_util(expr, i, j):
        #print("i=" + str(i) + "j=" + str(j) + "str(expr) = " + str(expr))
        if len(expr) == 1:
                if expr[0] in  matched:
                        return 0

                matched.append(expr[0])
                #print(str(expr[0]))
                return eval(str(expr[0]))

        if ((j < 0) or (j > len(expr))):
                return 0
        if ((i < 0) or (i > len(expr))):
                return 0

        temp = '('
        m = min(i, j)
        n = max(i, j)
        for k in range(m, n+1):
                temp += expr[k]
        del expr[m + 1 : n+1]
        temp += ')'
        expr[m] = temp
        i = m
        j = m - n

        return (countways_util(deepcopy(expr), i, i + 2) + countways_util(deepcopy(expr), i, i - 2))


def count_ways(expr):
        ways = 0
        for i in range(0, len(expr), 2):
                ways += countways_util(deepcopy(expr), i, i+2)
                ways += countways_util(deepcopy(expr), i, i-2)
                ways += countways_util(expr, i, i+2)
                ways += countways_util(expr, i, i-2)
        return ways

def no_of_ways(symbol, operator):
        expr = form_expr(symbol, operator)
        #print(str(expr))
        print(str(count_ways(expr)))

def test1(): # answer = 2
        no_of_ways(['T', 'F', 'T'], ['^', '&'])

def test2(): # answer = 2
        no_of_ways(['T', 'F', 'F'], ['^', '|'])

def test3(): # answer = 4
        no_of_ways(['T', 'T', 'F', 'T'], ['|', '&', '^'])

test1()
test2()
test3()



