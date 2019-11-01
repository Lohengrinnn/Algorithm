class Solution:
    def canMeasureWater(self, x: int, y: int, z: int) -> bool:
        dividend = max(x, y)
        divisor = min(x, y)
        while divisor > 0:
            quotient, reminder = divmod(dividend, divisor)
            dividend, divisor = divisor, reminder
        if dividend == 0:
            return z == 0
        return z <= x + y and z % dividend == 0



print(Solution().canMeasureWater(9, 2, 15))
print(Solution().canMeasureWater(9, 2, 19))
print(Solution().canMeasureWater(9, 2, 11))
print(Solution().canMeasureWater(2, 6, 5))
print(Solution().canMeasureWater(0, 2, 1))
print(Solution().canMeasureWater(0, 2, 2))
print(Solution().canMeasureWater(1, 1, 0))
print(Solution().canMeasureWater(13, 11, 1))
print(Solution().canMeasureWater(34, 5, 6))
print(Solution().canMeasureWater(0, 0, 0))
print(Solution().canMeasureWater(0, 0, 1))
