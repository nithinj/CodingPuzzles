from sys import stdin


inp = stdin.readline().split()
inp = [int(x) for x in inp]
(no_astro, pair) = (inp[0], inp[1])
comp_set = set()
list_of_sets = []
for i in range(no_astro):
    comp_set.add(i)
for i in range(pair):
    inp = stdin.readline().split()
    inp = [int(x) for x in inp]
    found = 0
    last_item = set()
    for item in list_of_sets:
        if ((inp[0] in item) or (inp[1] in item)):
            if found:
                last_item |= item
                list_of_sets.remove(item)
            item.add(inp[0])
            item.add(inp[1])
            found = 1
            last_item = item
    if (found == 0):
        temp_set = set()
        temp_set.add(inp[0])
        temp_set.add(inp[1])
        list_of_sets.append(temp_set)
total_set = set()
result = 0
count = 0
for item in list_of_sets:
    result += len(item) * count
    count += len(item)
    total_set |= item
if (comp_set != total_set):
    for i in range(len(comp_set - total_set)):
        result += count
        count += 1
print(str(result))
