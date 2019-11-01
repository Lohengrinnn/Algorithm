class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        r = num
        while r * r > num:
            r = (r + num/r) // 2
        return r * r == num


print(Solution().isPerfectSquare(4))
print(Solution().isPerfectSquare(5))
print(Solution().isPerfectSquare(0))