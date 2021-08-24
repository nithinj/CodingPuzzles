
def equal_subarray_zero_sum(arr):
        tot = sum(arr)
        sum_till = 0
        for i in range(len(arr)):
                if ((2 * sum_till + arr[i]) == tot):
                        return (arr[:i], arr[i+1:])
                sum_till += arr[i]

def test():
        # res = [6] and [3, 2, 1]
        print(str(equal_subarray_zero_sum([6, 2, 3, 2, 1])))
        # res = [6, 1] and [2, 5]
        print(str(equal_subarray_zero_sum([6, 1, 3, 2, 5])))
        # res = [] and [-2, -3, 2, 3]
        print(str(equal_subarray_zero_sum([6, -2, -3, 2, 3])))

test()