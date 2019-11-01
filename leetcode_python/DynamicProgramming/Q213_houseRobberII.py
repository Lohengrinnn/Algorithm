from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        prev1_with0, prev2_with0 = nums[0], 0
        prev1_without0, prev2_without0 = 0, 0
        for i in range(1, len(nums) - 1):
            tmp_prev1_with0, tmp_prev1_without0 = prev1_with0, prev1_without0
            prev1_with0 = max(prev2_with0 + nums[i], prev1_with0)
            prev1_without0 = max(prev2_without0 + nums[i], prev1_without0)
            prev2_with0 = tmp_prev1_with0
            prev2_without0 = tmp_prev1_without0
        return max(prev2_without0 + nums[-1], prev1_with0, prev1_without0)


print(Solution().rob([2,3,2]))
print(Solution().rob([3,2,2,4]))
print(Solution().rob([5,2,2,2,2,2,2,9]))