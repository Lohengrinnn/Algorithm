from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if not obstacleGrid:
            return 0
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        res: List[List[int]] = [[0] * n for i in range(m)]
        for row in range(m):
            if obstacleGrid[row][0]:
                break
            res[row][0] = 1
        for col in range(n):
            if obstacleGrid[0][col]:
                break
            res[0][col] = 1
        for row in range(1, m):
            for col in range(1, n):
                if obstacleGrid[row][col]:
                    continue
                res[row][col] = res[row - 1][col] + res[row][col - 1]
        return res[-1][-1]

ob = [
  [0,0,0],
  [0,1,0],
  [0,0,0]
]

print(Solution().uniquePathsWithObstacles(ob))