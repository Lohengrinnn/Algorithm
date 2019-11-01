from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        lv = nums[l]
        while l <= r:
            m = l + (r - l) // 2
            if nums[m] >= lv:
                l = m + 1
            else:
                r = m - 1
        return nums[l if l < len(nums) else 0]


print(Solution().findMin([3,4,5,0,1,2]))
print(Solution().findMin([3,4,5,1,2]))
print(Solution().findMin([5, 1,2,3,4]))
print(Solution().findMin([1]))