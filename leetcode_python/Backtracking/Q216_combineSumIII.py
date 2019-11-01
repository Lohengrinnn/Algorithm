from typing import List


class Solution:
    def combinationSum3_simple_bt(self, k: int, n: int) -> List[List[int]]:
        res = []
        def backtracking(sub_res, start):
            if sum(sub_res) == n and len(sub_res) == k:
                res.append(sub_res)
                return
            if sum(sub_res) > n or len(sub_res) == k:
                return
            for i in range(start, 10):
                backtracking(sub_res + [i], i + 1)
        backtracking([], 1)
        return res


    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        def backtracking(sub_res, start, sub_sum):
            if sum(sub_res) == 0 and 0 == k:
                res.append(sub_res)
                return
            if sum(sub_res) > n or len(sub_res) == k:
                return
            for i in range(start, 10):
                backtracking(sub_res + [i], i + 1, sub_sum - i)
        backtracking([], 1, n)
        return res

print(Solution().combinationSum3_simple_bt(3, 9))