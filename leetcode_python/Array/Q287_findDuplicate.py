from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        return self._findDuplicate(nums, 0, len(nums) - 1)


    def _findDuplicate(self, nums: List[int], l: int, r: int) -> int:
        while True:
            pivot, res = self.partition(nums, l, r)
            if res != 0:
                return res
            if nums[pivot] > pivot + 1:
                return self._findDuplicate(nums, pivot + 1, r)
            elif nums[pivot] < pivot + 1:
                return self._findDuplicate(nums, l, pivot - 1)
            else:
                res = self._findDuplicate(nums, pivot + 1, r)
                if res != 0:
                    return res
                return self._findDuplicate(nums, l, pivot - 1)

    def partition(self, nums: List[int], l: int, r: int) -> (int, int):
        i: int = l - 1
        pivot = nums[r]
        for j in range(l, r):
            if nums[j] < pivot:
                i += 1
                tmp = nums[i]
                nums[i] = nums[j]
                nums[j] = tmp
            elif nums[j] == pivot:
                return nums[j], nums[j]
        tmp = nums[i + 1]
        nums[i + 1] = pivot
        nums[r] = tmp
        return i + 1, 0


#print(Solution().findDuplicate([1, 3, 4, 2, 2]))
#print(Solution().findDuplicate([3, 1, 3, 4, 2]))
print(Solution().findDuplicate([1,1,9,5,4,2,7,3,6, 8]))