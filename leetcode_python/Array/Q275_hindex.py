from typing import List


class Solution:
    def hIndex1(self, citations: List[int]) -> int:
        l = 0
        n = len(citations)
        r = n - 1
        res = 0
        while True:
            if l > r:
                return res
            i = (l + r) // 2
            if citations[i] == n - i:
                return n - i
            elif citations[i] > n - i:
                res = n - i
                r = i - 1
            elif citations[i] < n - i:
                l = i + 1

    # this question's main concern is easy, if cita[i] >= n - i, then n - i is h-index
    # but n - i might not be the max h-index, for example [1, 5, 5]
    # cita[2] = 5 >= 3 - 2, but cita[1] = 5 >= 3 - 1, then 1, 2 are both h-index, 2 is max h-index
    # so my first solution is save a res, then return the latest updated res
    # when a h-index is found, r should be updated, which means next step
    # will find in smaller scope of i, n - i will be larger
    # if the h-index is max h-index, then r should never be updated, l always be updated
    # since the stop condition is l > r, and r = i - 1 when i is the h-index's index
    # l will ultimately become i to stop.
    def hIndex(self, citations: List[int]) -> int:
        l = 0
        n = len(citations)
        r = n - 1
        while l <= r:
            i = (l + r) // 2
            #if citations[i] == n - i:
                #return n - i
            if citations[i] >= n - i:
                r = i - 1
            else:
                l = i + 1
        return n - l

#print(Solution().hIndex([0, 1, 3, 5, 6]))
#print(Solution().hIndex([0, 1, 3, 5, 5, 5, 5, 6]))
#print(Solution().hIndex([0, 1, 3, 5, 5, 5, 5, 5, 6]))
print(Solution().hIndex([0, 0, 3, 3, 3]))
#print(Solution().hIndex([]))
#print(Solution().hIndex([0]))
#print(Solution().hIndex([1, 1]))