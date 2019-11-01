from typing import List


class Solution:
    def combinationSum4_backtracking(self, nums: List[int], target: int) -> int:
        res = 0
        def backtracking(sub_res):
            nonlocal res
            s = sum(sub_res)
            if s == target:
                res += 1
            elif s > target:
                return
            for i in nums:
                backtracking(sub_res + [i])
        backtracking([])
        return res


    def combinationSum4(self, nums: List[int], target: int) -> int:
        nums = sorted(nums)
        res = [0] * (target + 1)
        res[0] = 1
        for i in range(1, target + 1):
            for num in nums:
                if num > i:
                    break
                res[i] += res[i - num]
        return res[target]


print(Solution().combinationSum4_backtracking([1,2,3], 4))