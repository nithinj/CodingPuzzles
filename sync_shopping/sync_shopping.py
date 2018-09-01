from copy import deepcopy

DBG = 1


class Path:

    def __init__(self, dest, cost):
        self.dest = dest
        self.cost = cost


class City:

    def __init__(self):
        self.fish = 0
        self.paths = []
        self.bags = []


class Traverse:

    def __init__(self):
        self.cost = 0
        self.fishes = 0
        self.path = []


def dfs(city, cost, travel):
    global N, cities, travel_diary, K

    travel.path.append(city)
    travel.fishes += cities[city].fish
    travel.cost += cost
    if DBG:
        print(str(travel.path))
    if city == N - 1:
        travel_diary.append(travel)
        return
    for path in cities[city].paths:
        if path.dest not in travel.path:
            if DBG:
                print("path:" + str(path.dest))
            dfs(path.dest, path.cost, deepcopy(travel))
        elif travel.fishes < K:
            dfs(path.dest, path.cost, deepcopy(travel))


inp = [int(x) for x in input().split()]
[N, M, K] = inp[:]
cities = []
for i in range(N):
    inp = [int(x) for x in input().split()]
    cities.append(City())
    cities[i].fish = inp[0]
    for j in range(inp[0]):
        cities[i].bags.append(inp[j + 1])
for i in range(M):
    inp = [int(x) for x in input().split()]
    cities[inp[0] - 1].paths.append(Path(inp[1] - 1, inp[2]))
    cities[inp[1] - 1].paths.append(Path(inp[0] - 1, inp[2]))

travel_diary = []
dfs(0, 0, Traverse())
sorted(travel_diary, key=lambda arg: arg.cost)
if DBG:
    print(str(len(travel_diary)))

if (len(travel_diary) == 1) and (travel_diary[0].fishes >= K):
    print(str(travel_diary[j].cost))
    exit(0)


for i in range(1, len(travel_diary)):
    for j in range(i):
        fishes = 0
        if (travel_diary[j].fishes >= K) or (travel_diary[i].fishes >= K):
            print(str(travel_diary[j].cost))
            exit(0)
        else:  # need to apply set operations. check for fish bags only in the intersection
            # count = 2 if bags contains >1 else count = 1
            # same logic has to be applied when you found just a single path,
            # and to all the elements. so better make a fun()
            res = list(set(travel_diary[i].path + travel_diary[j].path))
            for item in res:
                fishes += cities[item].fish
                if fishes >= K:
                    print(str(travel_diary[j].cost))
                    exit(0)
