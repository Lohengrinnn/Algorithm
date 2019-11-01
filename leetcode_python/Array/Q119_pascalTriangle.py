from typing import List


class Solution:
    def getRow1(self, rowIndex: int) -> List[int]:
        res = [1]
        for i in range(1, rowIndex + 1):
            res = [1] + [res[j] + res[j + 1] for j in range(i - 1)] + [1]
        return res


    def getRow(self, rowIndex: int) -> List[int]:
        res = []
        for i in range(0, rowIndex + 1):
            res = [1] + res
            if i >= 2:
                for j in range(1, i):
                    res[j] += res[j + 1]
        return res

print(Solution().getRow(5))