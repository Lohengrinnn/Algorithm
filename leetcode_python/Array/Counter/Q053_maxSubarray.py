from typing import List
import sys

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        sum = res = -sys.maxsize - 1
        for num in nums:
            if sum < 0:
                sum = num
            else:
                sum += num
            res = max(res, sum)
        return res


print(Solution().maxSubArray([2]))
print(Solution().maxSubArray([-2,-1,-3]))
print(Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
