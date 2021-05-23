def find_missing_num(arr):
    sum = 0
    for i in range(1, len(arr) + 1):
        sum += i - arr[i-1]
    return sum + len(arr) + 1

if __name__ == '__main__':
    inp = [int(x) for x in input().split()]
    res = find_missing_num(inp)
    print(str(res))