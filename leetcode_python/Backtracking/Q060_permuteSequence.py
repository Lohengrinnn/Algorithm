from typing import List
import math

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        remnant = list(range(1, n + 1))
        res = ''
        k -= 1
        for i in range(n, 0, -1):
            quotient, k = divmod(k, math.factorial(i - 1))
            dig = remnant[quotient]
            res += '%s' % dig
            remnant.remove(dig)
        return res


print(Solution().getPermutation(4, 5))


