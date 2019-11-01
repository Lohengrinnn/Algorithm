class Solution:
    def climbStairs(self, n: int) -> int:
        res_last = 1
        res = 1
        for _ in range(1, n):
            res, res_last = res + res_last, res
        return res


print(Solution().climbStairs(3))