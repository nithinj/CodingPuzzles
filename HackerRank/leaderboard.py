from sys import stdin


n = int(stdin.readline())
inp = stdin.readline().split()
inp = [int(x) for x in inp]
s = list(set(inp))
s = sorted(s, reverse=True)

m = int(stdin.readline())
inp = stdin.readline().split()
inp = [int(x) for x in inp]

count = len(s)
for i in inp:
    while (count > 0):
        if s[count - 1] < i:
            count -= 1
        else:
            if (s[count - 1] > i):
                print(str(count + 1))
            else:
                print(str(count))
            break
    if (count == 0):
        print(str(count + 1))
