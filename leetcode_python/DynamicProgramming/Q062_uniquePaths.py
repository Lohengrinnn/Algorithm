from typing import List


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        res: List[List[int]] = [[0] * n] * m
        for row in range(m):
            res[row][0] = 1
        for col in range(n):
            res[0][col] = 1
        for row in range(1, m):
            for col in range(1, n):
                res[row][col] = res[row - 1][col] + res[row][col - 1]
        return res[-1][-1]


print(Solution().uniquePaths(3, 3))