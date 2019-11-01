from typing import List

class Solution:
    def subsetsWithDup1(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        res = []
        upper = []
        def backtracking(start):
            if upper not in res:
                res.append(upper[:])
            for i in range(start, len(nums)):
                upper.append(nums[i])
                backtracking(i + 1)
                upper.pop()
        backtracking(0)
        return res


    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        res = [[]]
        for i in range(len(nums)):
            if i == 0 or nums[i] != nums[i - 1]:
                l = len(res)
            for item in range(len(res) - l, len(res)):
                res.append(res[item] + [nums[i]])
        return res


print(Solution().subsetsWithDup([2,1,2]))