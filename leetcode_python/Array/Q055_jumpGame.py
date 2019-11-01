from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if not nums:
            return False
        reachable = nums[0]
        for i in range(1, len(nums)):
            if i > reachable:
                return False
            if i + nums[i] > reachable:
                reachable = i + nums[i]
        return True


print(Solution().canJump([2,3,1,1,0]))
print(Solution().canJump([3,2,1,0,4]))