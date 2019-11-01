from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        c = None
        for n in nums:
            if n != c or c == None:
                nums[i] = n
                i += 1
                c = n
        return i


print(Solution().removeDuplicates([1, 1, 1, 1]), 1)
print(Solution().removeDuplicates([1, 1, 1, 2]), 2)
print(Solution().removeDuplicates([1, 1, 2, 2]), 2)
print(Solution().removeDuplicates([]), 0)
