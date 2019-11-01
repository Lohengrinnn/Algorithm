from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates = sorted(candidates)
        res = []
        def backtracking(cmb, start):
            s = sum(cmb)
            if s == target:
                res.append(cmb)
            elif s > target:
                return
            for i in range(start, len(candidates)):
                if i == start or candidates[i] != candidates[i - 1]:
                    backtracking(cmb + [candidates[i]], i + 1)
        backtracking([], 0)
        return res


print(Solution().combinationSum2([10,1,2,7,6,1,5], 8))