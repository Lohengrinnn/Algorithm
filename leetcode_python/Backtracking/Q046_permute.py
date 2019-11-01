from typing import List


class Solution:
    def permute1(self, nums: List[int]) -> List[List[int]]:
        res, to_do = [], [([], nums)]
        while to_do:
            used, remnant = to_do.pop()
            if len(remnant) == 0:
                res.append(used)
            for i in range(len(remnant)):
                r = remnant[:]
                r.pop(i)
                to_do.append((used + [remnant[i]], r))
        return res

    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(used, remnant):
            if not remnant:
                res.append(used)
            for i in range(len(remnant)):
                r = remnant[:]
                r.pop(i)
                dfs(used + [remnant[i]], r)
        dfs([], nums)
        return res


print(Solution().permute([1,2,3]))