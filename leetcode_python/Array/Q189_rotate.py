from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        if l == 0:
            return
        k = k % l
        s = nums[l - k:]
        for n in range(l - 1, k - 1, -1):
            nums[n] = nums[n - k]
        nums[:k] = s[:]

nums = [1, 2, 3, 4, 5]
print(nums)
Solution().rotate(nums, 3)
print(nums)

nums = [1, 2, 3, 4, 5]
print(nums)
Solution().rotate(nums, 0)
print(nums)

nums = []
print(nums)
Solution().rotate(nums, 3)
print(nums)