from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        d = [0 for i in range(len(nums))]
        for n in nums:
            if len(nums) >= n > 0:
                d[n - 1] = 1
        for i in range(len(d)):
            if d[i] == 0:
                return i + 1
        return len(d) + 1


nums = [1, 2, 3]
print(Solution().firstMissingPositive(nums), 4)

nums = [1, 3, 0, -1]
print(Solution().firstMissingPositive(nums), 2)

nums = []
print(Solution().firstMissingPositive(nums), 1)