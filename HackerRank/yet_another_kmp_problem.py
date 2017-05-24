from sys import stdin
import string


inp = stdin.readline().split()
inp = [int(x) for x in inp]
alpha = list(string.ascii_lowercase)
dic = {}
out = []
for i, j in enumerate(inp):
    if j not in dic:
        dic[j] = []
    dic[j].append([alpha[i], j])
sorted_inp = sorted(inp)
sorted_inp = [x for x in sorted_inp if x != 0]
out.append(dic[sorted_inp[0]][0][0])
dic[sorted_inp[0]][0][1] = dic[sorted_inp[0]][0][1] - 1
for elem in inp:
    item = dic[elem][0]
    next_item = None
    while item[1] != 0:
        if ((len(sorted_inp) > 1) and (sorted_inp[0] == elem) and
                (len(out) >= 2) and (out[0] == out[-1]) and (out[0] == item[0])
                and (out[0] == out[1])):
            if next_item is None:
                inp_nonzero = [x for x in inp if x != 0]
                if dic[inp_nonzero[1]] == elem:
                    next_item = dic[elem][1]
                else:
                    next_item = dic[inp_nonzero[1]][0]
            out.append(next_item[0])
            next_item[1] = next_item[1] - 1
        out.append(item[0])
        item[1] = item[1] - 1
    del dic[elem][0]

print(''.join(out))
