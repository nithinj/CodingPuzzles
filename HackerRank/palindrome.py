from sys import stdin


inp = stdin.readline().split()
inp = [int(x) for x in inp]
n = inp[0]
k = inp[1]
num = list(stdin.readline())
mid = int(n / 2)
if (n % 2 == 0):
    r = mid
    l = r - 1
else:
    r = mid + 1
    l = mid - 1
changes = 0
while (l >= 0):
    if (num[l] != num[r]):
        if (num[l] == '9' or num[r] == '9'):
            num[l] = '9'
            num[r] = '9'
            k -= 1
            changes -= 1
        changes += 1
    l -= 1
    r += 1
if (k < changes):
    print('-1')
    exit(0)
l = 0
r = n - 1
conversion = k - changes
while ((changes > 0 or conversion > 0) and (l <= r)):
    if ((l == r) or (num[l] != num[r])):
        if (conversion > 0 and num[l] != '9'):
            num[l] = '9'
            num[r] = '9'
            conversion -= 1
            changes -= 1
    elif (conversion > 1 and num[l] != '9'):
        num[l] = '9'
        num[r] = '9'
        conversion -= 2

    if (int(num[l]) < int(num[r])):
        num[l] = num[r]
        changes -= 1
    elif (int(num[l]) > int(num[r])):
        num[r] = num[l]
        changes -= 1
    l += 1
    r -= 1


print(''.join(num))
