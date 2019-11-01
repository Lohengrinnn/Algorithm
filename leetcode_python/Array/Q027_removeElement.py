from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        for n in nums:
            if n != val:
                nums[i] = n
                i += 1
        return i


print(Solution().removeElement([1, 1], 1), 0)
print(Solution().removeElement([1, 2], 1), 1)
print(Solution().removeElement([2, 1], 1), 1)
print(Solution().removeElement([], 1), 0)
