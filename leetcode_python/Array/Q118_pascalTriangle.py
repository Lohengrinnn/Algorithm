from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = list()
        for i in range(numRows):
            if i == 0:
                res.append([1])
            else:
                res.append([1 if (j == 0 or j == i) else (res[i - 1][j - 1] + res[i - 1][j]) for j in range(i + 1)])
        return res


print(Solution().generate(7))