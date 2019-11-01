from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        cur = [None, None]
        for num in nums:
            if cur[0] != num:
                cur[0] = num
            elif cur[1] != num:
                cur[1] = num
            else:
                continue
            nums[i] = num
            i += 1
        return i


nums = [1, 1, 1, 2, 2, 3]
print(nums)
i = Solution().removeDuplicates(nums)
print(i, nums[:i])

nums = [1, 1, 1, 1, 1, 1, 1]
print(nums)
i = Solution().removeDuplicates(nums)
print(i, nums[:i])