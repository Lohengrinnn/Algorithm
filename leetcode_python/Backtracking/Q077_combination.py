from typing import List


class Solution:
    def combine1(self, n: int, k: int) -> List[List[int]]:
        res = []
        def backtracking(start, cmbn):
            if len(cmbn) == k:
                res.append(cmbn[:])
                return
            for i in range(start, n + 1):
                backtracking(i + 1, cmbn + [i])
        backtracking(1, [])
        return res


    def combine_backtracking_two_case(self, n: int, k: int) -> List[List[int]]:
        res = []
        def backtracking(i, cmbn):
            if len(cmbn) == k:
                res.append(cmbn[:])
                return
            if i == n + 1:
                return
            backtracking(i + 1, cmbn + [i])
            backtracking(i + 1, cmbn)
        backtracking(1, [])
        return res


    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        sub_res = [[]]
        for i in range(1, n + 1):
            for j in range(len(sub_res)):
                sub_res.append(sub_res[j] + [i])
            for j in range(len(sub_res) - 1, -1, -1):
                if len(sub_res[j]) == k:
                    res.append(sub_res.pop(j))
        return res


print(Solution().combine(4, 2))