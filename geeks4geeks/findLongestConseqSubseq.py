
def findLongestConseqSubseq(arr):
        S = set()
        max_len = 0
        for num in arr:
                S.add(num)

        for num in arr:
                if S.__contains__(num):
                        j = num
                        while S.__contains__(j):
                                j += 1
                
                        max_len = max(max_len, j - num)
        
        return max_len


def test():
        #result = 3 [92, 93, 94 ]
        print(str(findLongestConseqSubseq([ 1, 94, 93, 1000, 5, 92, 78 ])))
        #result = 4 [4, 5, 6, 7]
        print(str(findLongestConseqSubseq([ 1, 5, 92, 4, 78, 6, 7])))

test()