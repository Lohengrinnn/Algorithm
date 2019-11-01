import sys
from typing import List


class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        dp: List[List[int]] = [[0] * len(nums) for i in range(len(nums))]
        for j in range(2, len(nums)):
            for i in range(j - 2, - 1, -1):
                for m in range(i + 1, j):
                    dp[i][j] = max(dp[i][j], nums[m] * nums[i] * nums[j] + dp[i][m] + dp[m][j])
        return dp

print(Solution().maxCoins([3,2,3]))