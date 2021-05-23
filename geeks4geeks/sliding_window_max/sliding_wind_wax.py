def sliding_wind_max(arr, wind_sz):
    meta = [0]
    out = []

    for i in range(len(arr)):
        
        wind_start = i - wind_sz + 1
        if (wind_start < 0):
            wind_start = 0

        if arr[i] > arr[meta[0]]:
            meta = [i]
        elif len(meta) == 1:
            meta.append(i)
        elif arr[i] > arr[meta[1]]:
            meta[1] = i

        # member not belongs to the window.
        if (wind_start > meta[0]):
            meta.pop(0)
            meta.append(i)

        if (i >= wind_sz - 1):
            out.append(arr[meta[0]])

        #print("i=" + str(i) + "  wind_start=" + str(wind_start) + "  meta list="+str(meta))

    return out


if __name__ == '__main__':
    inp = [int(x) for x in input().split()]
    k = int(input())
    res = sliding_wind_max(inp, k)
    print(" ".join(map(str, res)))