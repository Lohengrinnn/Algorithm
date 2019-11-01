from typing import List


class Solution:
    def minimumTotal1(self, triangle: List[List[int]]) -> int:
        for i in range(1, len(triangle)):
            for j in range(i + 1):
                if j == 0:
                    triangle[i][j] += triangle[i - 1][j]
                elif j == i:
                    triangle[i][j] += triangle[i - 1][j - 1]
                else:
                    triangle[i][j] += min(triangle[i - 1][j - 1], triangle[i - 1][j])
        return min(triangle[-1])

    def minimumTotal(self, triangle: List[List[int]]) -> int:
        for i in range(1, len(triangle)):
            for j in range(i + 1):
                triangle[i][j] += min(triangle[i - 1][0 if j == 0 else j - 1 : j + 1])
        return min(triangle[-1])

t = [
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]

print(Solution().minimumTotal(t))