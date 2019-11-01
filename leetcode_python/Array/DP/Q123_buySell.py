import sys
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit_buy1 = profit_buy2 = -sys.maxsize
        profit_sell1 = profit_sell2 = 0
        for price in prices:
            profit_sell2 = max(profit_sell2, profit_buy2 + price)
            profit_buy2 = max(profit_buy2, profit_sell1 - price)
            profit_sell1 = max(profit_sell1, profit_buy1 + price)
            profit_buy1 = max(profit_buy1, -price)
        return profit_sell2



print(Solution().maxProfit([1,2,3,4,5]))
print(Solution().maxProfit([1,2,3,2,5]))
print(Solution().maxProfit([1,2,4,2,5,7,2,4,9,0]))