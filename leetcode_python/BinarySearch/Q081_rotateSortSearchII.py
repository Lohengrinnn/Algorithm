import sys
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        def _search(start: int, end: int) -> bool:
            if start > end:
                return False
            m = start + (end - start) // 2
            if nums[m] == target or nums[start] == target:
                return True
            if nums[m] == nums[start] == nums[end]:
                return _search(start, m - 1) or _search(m + 1, end)
            num = nums[m]
            if nums[m] >= nums[start] and target < nums[start]:
                num = -sys.maxsize - 1
            elif nums[m] < nums[start] and target > nums[start]:
                num = sys.maxsize
            if num > target:
                return _search(start, m - 1)
            else:
                return _search(m + 1, end)
        return _search(0, len(nums) - 1)

print(Solution().search([4,5,6,7,0,1,2], 2))
print(Solution().search([1, 3, 1, 1, 1], 3))

print(Solution().search([2,4,5,6,7,7,0,1,2], 7))

print(Solution().search([4,5,6,7,0,1,2], 3))
print(Solution().search([], 2))
