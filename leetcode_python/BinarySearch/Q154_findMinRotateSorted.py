from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        def _findMin(l: int, r: int) -> int:
            if nums[l] < nums[r] or l == r:
                return nums[l]
            m = l + (r - l) // 2
            if nums[m] > nums[l]:
                return _findMin(m + 1, r)
            elif nums[m] < nums[l]:
                return _findMin(l + 1, m)
            else:
                if nums[r] == nums[l]:
                    return min(_findMin(l, m), _findMin(m + 1, r))
                else:
                    return _findMin(m + 1, r)
        return _findMin(0, len(nums) - 1)


print(Solution().findMin([2,2,2,1,2,2,2]))
print(Solution().findMin([2,2,2,1,2,2]))
print(Solution().findMin([1,2,2,2,2,2]))