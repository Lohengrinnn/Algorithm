from typing import List
import sys


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxBuy = -sys.maxsize - 1
        maxSell = 0
        maxCooldown = 0
        for price in prices:
            prev_maxCooldown = maxCooldown
            maxCooldown = max(maxCooldown, maxSell)
            maxSell = max(maxSell, maxBuy + price)
            maxBuy = max(maxBuy, prev_maxCooldown - price)
        return maxSell


print(Solution().maxProfit([1,2,3,0,2]))
print(Solution().maxProfit([]))
print(Solution().maxProfit([1]))
print(Solution().maxProfit([1,2]))
print(Solution().maxProfit([1,2,3,0,2,3]))