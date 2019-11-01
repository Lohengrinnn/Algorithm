from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        res = []
        def dfs(used, remnant):
            if not remnant:
                res.append(used)
            for i in range(len(remnant)):
                if i == 0 or remnant[i] != remnant[i - 1]:
                    r = remnant[:]
                    r.pop(i)
                    dfs(used + [remnant[i]], r)
        dfs([], nums)
        return res


print(Solution().permuteUnique([1,1,2]))