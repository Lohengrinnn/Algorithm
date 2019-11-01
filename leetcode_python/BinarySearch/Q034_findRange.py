from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        l = 0
        r = len(nums) - 1
        m = 0
        while l <= r:
            m = l + (r - l) // 2
            if nums[m] > target:
                r = m - 1
            elif nums[m] < target:
                l = m + 1
            else:
                break
        if nums[m] != target:
            return [-1, -1]
        save_r = r
        save_m = m
        r = m
        while l <= r:
            m = l + (r - l) // 2
            if nums[m] < target:
                l = m + 1
            else:
                r = m - 1
        targe_l = l
        l = save_m
        r = save_r
        while l <= r:
            m = l + (r - l) // 2
            if nums[m] > target:
                r = m - 1
            else:
                l = m + 1
        return [targe_l, r]

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def searchForInsert(t):
            l = 0
            r = len(nums) - 1
            while l <= r:
                m = l + (r - l) // 2
                if nums[m] >= t:
                    r = m - 1
                else:
                    l = m + 1
            return l
        lot = searchForInsert(target)
        return [lot, searchForInsert(target + 1) - 1] if target in nums[lot:] else [-1, -1]

print(Solution().searchRange([1,3,4,4,4,4,4,4,4,4], 4))
print(Solution().searchRange([1], 1))