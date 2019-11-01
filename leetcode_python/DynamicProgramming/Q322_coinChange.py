import sys
from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp: List[int] = [0] + [-1] * amount
        for i in range(1, amount + 1):
            dp_i = sys.maxsize
            for coin in coins:
                if i >= coin and dp[i - coin] != -1:
                    dp_i = min(dp_i, 1 + dp[i - coin])
            if dp_i != sys.maxsize:
                dp[i] = dp_i
        return dp[-1]


print(Solution().coinChange([2,5], 8))