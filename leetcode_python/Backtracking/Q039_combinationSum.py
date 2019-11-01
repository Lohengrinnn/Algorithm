from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def backtracking(cmb, start):
            s = sum(cmb)
            if s == target:
                res.append(cmb)
            elif s > target:
                return
            for i in range(start, len(candidates)):
                backtracking(cmb + [candidates[i]], i)
        backtracking([], 0)
        return res


print(Solution().combinationSum([2,3,7], 7))