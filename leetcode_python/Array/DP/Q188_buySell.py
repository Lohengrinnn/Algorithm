from typing import List
import sys


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if k > len(prices) // 2:
            res = 0
            buy = -sys.maxsize - 1
            sell = 0
            for price in prices:
                if price + buy < sell:
                    res += sell
                    buy = -price
                    sell = 0
                else:
                    sell = price + buy
                buy = max(-price, buy)
            return res + sell
        if k == 0:
            return 0
        buy_profit = [-sys.maxsize - 1] * k
        sell_profit = [0] * k
        for price in prices:
            for i in range(k-1, -1, -1):
                sell_profit[i] = max(sell_profit[i], buy_profit[i] + price)
                buy_profit[i] = max(buy_profit[i], sell_profit[i - 1] - price if i > 0 else -price)
        return sell_profit[-1]


print(Solution().maxProfit(2, [3,4,5,1,9,1,7]))
print(Solution().maxProfit(2, [3,4,5,1,9,1,7,1,8]))
print(Solution().maxProfit(3, [3,4,5,1,9,1,7,1,8,2,11]))
print(Solution().maxProfit(0, [1,2]))
print(Solution().maxProfit(6, [1,2,4,1,6,1,8]))
