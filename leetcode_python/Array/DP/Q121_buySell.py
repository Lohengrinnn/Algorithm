from typing import List
import sys

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice, maxProfit = sys.maxsize, 0
        for p in prices:
            minPrice = min(minPrice, p)
            maxProfit = max(p - minPrice, maxProfit)
        return maxProfit

    def maxProfit2(self, prices: List[int]) -> int:
        maxSell = 0
        maxHold = 0
        for i in range(1, len(prices)):
            diff = prices[i] - prices[i - 1]
            maxHold = max(maxHold + diff, 0)
            maxSell = max(maxSell, maxHold)
        return maxSell

    def maxProfit1(self, prices: List[int]) -> int:
        profits = [prices[i + 1] - prices[i] for i in range(len(prices) - 1)]
        total_profit = 0
        sell_profit = 0
        for p in profits:
            if p < 0 and sell_profit < total_profit:
                sell_profit = total_profit
            total_profit += p
            if total_profit < 0:
                total_profit = 0
        return max(total_profit, sell_profit)


print(Solution().maxProfit([7,1,3,2,6,5]))
print(Solution().maxProfit1([7,1,3,2,6,5]))
print(Solution().maxProfit([1,4,3,7,2,4,6,8,4,7]))
print(Solution().maxProfit1([1,4,3,7,2,4,6,8,4,7]))