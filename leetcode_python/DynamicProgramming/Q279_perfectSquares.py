import math
import sys


class Solution:
    def numSquares1(self, n: int) -> int:
        squares = [i * i for i in range(1, round(math.sqrt(n)) + 1)]
        res = [0] + [sys.maxsize] * n
        for i in range(1, n + 1):
            for square in squares:
                if i < square:
                    break
                res[i] = min(res[i], res[i - square] + 1)
        return res[n]
    _memo = {0: 0}
    def numSquares(self, n: int) -> int:
        squares = [i * i for i in range(1, round(math.sqrt(n)) + 1)]
        memo = self._memo
        def _numSquares(n: int) -> int:
            if n in memo:
                return memo[n]
            res = sys.maxsize
            for square in reversed(squares):
                if square <= n:
                    if n // square > res:
                        break
                    res = min(res,  _numSquares(n - square) + 1)
            memo[n] = res
            return res
        return _numSquares(n)

import datetime
dt = datetime.datetime.now()
print(Solution().numSquares(128))
print(Solution().numSquares(7334))
print(datetime.datetime.now() - dt)
dt = datetime.datetime.now()
print(Solution().numSquares(7334))
print(datetime.datetime.now() - dt)