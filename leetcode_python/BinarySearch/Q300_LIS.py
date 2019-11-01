from typing import List
import sys


class Solution:
    def lengthOfLIS1(self, nums: List[int]) -> int:
        res = 0
        lis = []
        for i in nums:
            l, r = 0, len(lis) - 1
            while l <= r:
                m = l + (r - l) // 2
                if lis[m][0] >= i:
                    r = m - 1
                else:
                    l = m + 1
            lis_i = 1
            for j in range(l):
                lis_i = max(lis[j][1] + 1, lis_i)
            if l < len(lis) and lis[l][0] == i:
                lis[l][1] = lis_i
            else:
                lis.insert(l, [i, lis_i])
            res = max(res, lis_i)
        return res

    def lengthOfLIS(self, nums: List[int]) -> int:
        lis_tails = []
        for num in nums:
            l, r = 0, len(lis_tails) - 1
            while l <= r:
                m = l + (r - l) // 2
                if lis_tails[m] >= num:
                    r = m - 1
                else:
                    l = m + 1
            if l < len(lis_tails):
                lis_tails[l] = num
            else:
                lis_tails.append(num)
        return len(lis_tails)

print(Solution().lengthOfLIS([10,9,2,5,3]))
print(Solution().lengthOfLIS([10,9,2,5,3,7,101,18]))