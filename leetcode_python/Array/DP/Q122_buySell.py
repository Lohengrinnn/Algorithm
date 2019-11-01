from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        for i in range(1, len(prices)):
            res += max(prices[i] - prices[i - 1], 0)
        return res

    def maxProfit1(self, prices: List[int]) -> int:
        profits = [prices[i+1] - prices[i] for i in range(len(prices) - 1)]
        return sum([p for p in profits if p > 0])


print(Solution().maxProfit([7,1,3,2,6,5]))
print(Solution().maxProfit([1,4,3,7,2,4,6,8,4,7]))
print(Solution().maxProfit([]))