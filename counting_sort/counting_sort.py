from sys import stdin


key_val = {}
max = 0
n = int(stdin.readline())
for i in range(n):
    inp = stdin.readline().split()
    key = int(inp[0])
    if i < n / 2:
        val = '-'
    else:
        val = inp[1]
    if max < key:
        max = key
    if key in key_val:
        key_val[key].append(val)
    else:
        key_val[key] = [val]

out = ''
for i in range(max + 1):
    out += ' '.join(key_val[i])
    out += ' '
print(out)
