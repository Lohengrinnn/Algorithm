import sys
from typing import List


class Solution:
    def search1(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while l <= r:
            m = l + (r - l) // 2
            if nums[m] == target:
                return m
            elif nums[m] > target:
                if nums[l] < nums[r]:
                    r = m - 1
                else:
                    if target <= nums[r]:
                        if nums[m] < nums[r]:
                            r = m - 1
                        else:
                            l = m + 1
                    else:
                        r = m - 1
            else:
                if nums[l] < nums[r]:
                    l = m + 1
                else:
                    if target <= nums[r]:
                        l = m + 1
                    else:
                        if nums[m] < nums[l]:
                            r = m - 1
                        else:
                            l = m + 1
        return -1

    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            m = l + (r - l) // 2
            if nums[m] == target:
                return m
            num = nums[m]
            if nums[m] >= nums[l] and target < nums[l]:
                num = -sys.maxsize - 1
            elif nums[m] < nums[l] and target >= nums[l]:
                num = sys.maxsize
            if num > target:
                r = m - 1
            else:
                l = m + 1
        return -1

print(Solution().search([4,5,6,7,0,1,2], 2))
print(Solution().search([4,5,6,7,0,1,2], 4))

print(Solution().search([4,5,6,7,0,1,2], 7))

print(Solution().search([4,5,6,7,0,1,2], 3))
print(Solution().search([], 2))
