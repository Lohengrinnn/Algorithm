from typing import List

class Solution:
    def findPeakElement1(self, nums: List[int]) -> int:
        def leftIncrease(n):
            if n == 0:
                return True
            else:
                return nums[n] > nums[n - 1]
        def rightDecrease(n):
            if n == len(nums) - 1:
                return True
            else:
                return nums[n] > nums[n + 1]
        l, r = 0, len(nums) - 1
        while l < r:
            m = l + (r - l) // 2
            if rightDecrease(m):
                r = m
            elif leftIncrease(m):
                l = m + 1
            else:
                r = m - 1
        return r

    def findPeakElement(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        while l < r:
            m  = l + (r - l) // 2
            if m - 1 >= l and nums[m - 1] > nums[m]:
                r = m - 1
            elif m + 1 <= r and nums[m + 1] > nums[m]:
                l = m + 1
            else:
                return m
        return r

print(Solution().findPeakElement([1,2,3,1]))
print(Solution().findPeakElement([1,2,1,3,5,6,4]))
print(Solution().findPeakElement([1]))
print(Solution().findPeakElement([2, 1, 2]))