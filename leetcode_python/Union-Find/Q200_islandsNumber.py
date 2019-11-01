from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        rows = len(grid)
        cols = len(grid[0])
        res = 0
        for x in range(rows):
            for y in range(cols):
                if grid[x][y] == '1':
                    def bfs(i, j):
                        if 0 <= i < rows and 0 <= j < cols and grid[i][j] == '1':
                            grid[i][j] = '#'
                            bfs(i, j - 1)
                            bfs(i, j + 1)
                            bfs(i - 1, j)
                            bfs(i + 1, j)
                    bfs(x, y)
                    res += 1
        return res



print(Solution().numIslands([]))
print(Solution().numIslands([["1","1","1"],
                             ["0","1","0"],
                             ["1","1","1"]]))
print(Solution().numIslands([['1','1','1','1','0'],
                             ['1','1','0','1','0'],
                             ['1','1','0','0','0'],
                             ['0','0','0','0','0']]))
print(Solution().numIslands([['1','1','0','0','0'],
                             ['1','1','0','0','0'],
                             ['0','0','1','0','0'],
                             ['0','0','0','1','1'],
                             ['0','0','0','1','1']]))