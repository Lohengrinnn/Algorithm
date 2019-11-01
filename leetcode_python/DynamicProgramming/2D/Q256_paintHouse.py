from typing import List

class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        row = len(costs)
        res = [0] * 3
        for r in range(row):
            prev_res = res[:]
            for c in range(3):
                res[c] = min([prev_res[cd] + costs[r][c] for cd in range(3) if cd != c])
        return min(res)


print(Solution().minCost([[17,2,17],[16,16,5],[14,3,19]]))