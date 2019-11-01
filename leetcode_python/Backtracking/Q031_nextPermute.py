from typing import List


class Solution:
    def reverse(self, nums, start):
        for k in range(start, (len(nums) + start) // 2):
            rival = len(nums) - 1 - k + start
            tmp = nums[k]
            nums[k] = nums[rival]
            nums[rival] = tmp

    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        find = False
        for i in range(len(nums) - 2, -1, -1):
            for j in range(len(nums) - 1, i, -1):
                if nums[j] > nums[i]:
                    tmp = nums[i]
                    nums[i] = nums[j]
                    nums[j] = tmp
                    find = True
                    break
            if find:
                break
        reverse_start = i + 1 if find else 0
        for k in range(reverse_start, (len(nums) + reverse_start) // 2):
            rival = len(nums) - 1 - k + reverse_start
            tmp = nums[k]
            nums[k] = nums[rival]
            nums[rival] = tmp


#nums = [1, 2, 3]
nums = [3, 2, 1]
nums = [2, 3, 1]
#nums = [1, 2]
#nums = [1, 4, 5, 3]
#nums = [1]
Solution().nextPermutation(nums)
#Solution().reverse(nums, 1)
print(nums)
