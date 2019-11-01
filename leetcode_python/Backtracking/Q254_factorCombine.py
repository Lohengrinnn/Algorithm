from typing import List


class Solution:
    def getFactors1(self, n: int) -> List[List[int]]:
        res = []
        def backtracking(pro, sub_res, start):
            if start <= pro < n:
                res.append(sub_res + [pro])
            while start * start <= pro:
                quotient, remainder = divmod(pro, start)
                if remainder == 0:
                    backtracking(quotient, sub_res + [start], start)
                start += 1
        backtracking(n, [], 2)
        return res

    def getFactors(self, n: int) -> List[List[int]]:
        res = []
        for i in range(0, n):
            pass


print(Solution().getFactors1(100))
print(Solution().getFactors1(1))
print(Solution().getFactors1(23848713))