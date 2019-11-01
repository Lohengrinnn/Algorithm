class Solution:
    def myPow1(self, x: float, n: int) -> float:
        is_neg = n < 0
        n = abs(n)
        dp = {1: x}
        i = 1
        res = 1
        while i < n:
            dp[i * 2] = dp[i] * dp[i]
            i = i * 2
        while n > 0:
            while i > n:
                i /= 2
            n -= i
            res *= dp[i]
        return 1 / res if is_neg else res

    def myPow(self, x: float, n: int) -> float:
        is_neg = n < 0
        n = abs(n)
        res = 1
        while n > 0:
            if n & 1:
                res *= x
            n >>= 1
            x *= x
        return 1 / res if is_neg else res


print(Solution().myPow(3.0, 5))
print(Solution().myPow(3.0, 6))
print(Solution().myPow(3.0, -5))
print(Solution().myPow(3.0, 0))