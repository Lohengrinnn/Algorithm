from typing import List


class Solution:
    def rob1(self, nums: List[int]) -> int:
        if not nums:
            return 0
        elif len(nums) == 1:
            return nums[0]
        m = [0] * len(nums)
        for i in range(len(nums)):
            if i < 2:
                m[i] = nums[i]
            if i >= 2:
                m[i] = m[i - 2] + nums[i]
            if i >= 3:
                m[i] = max(m[i], m[i - 3] + nums[i])
        return max(m[-1], m[-2])


    def rob2(self, nums: List[int]) -> int:
        if not nums:
            return 0
        elif len(nums) == 1:
            return nums[0]
        m = [0] * len(nums)
        m[0] = nums[0]
        m[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            m[i] = max(m[i - 1], m[i - 2] + nums[i])
        return m[-1]


    def rob(self, nums: List[int]) -> int:
        prev1, prev2, m = 0, 0, 0
        for i in range(len(nums)):
            m = max(prev1, prev2 + nums[i])
            prev2 = prev1
            prev1 = m
        return m


print(Solution().rob([2, 2, 9, 3, 1, 3]))
print(Solution().rob([2, 1, 1, 2]))
print(Solution().rob1([2, 2, 9, 3, 1, 3]))
print(Solution().rob1([2, 1, 1, 2]))