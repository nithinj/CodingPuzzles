
def mincost(cost, m, n):
        for i in range(1, m):
                cost[i][0] += cost[i-1][0]

        for i in range(1, n):
                cost[0][i] += cost[0][i-1]

        for i in range(1, m):
                for j in range(1, n):
                        cost[i][j] += min(cost[i-1][j-1], cost[i][j-1], cost[i-1][j])

        return cost[m-1][n-1]


def test1():
        cost = [[1, 2, 3], [4, 8, 2], [1, 5, 3]]
        print(str(mincost(cost, len(cost), len(cost[0]))))

if __name__ == '__main__':
        test1()