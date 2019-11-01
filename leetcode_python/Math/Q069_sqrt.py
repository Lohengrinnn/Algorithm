class Solution:
    def mySqrt1(self, x: int) -> int:
        if x == 0:
            return 0
        len_digit = 0
        q = x
        while q > 0:
            q = q // 10
            len_digit += 1
        exp = (len_digit - 1) // 2
        l, r = pow(10, exp), pow(10, exp + 1)
        while l <= r:
            m = (l + r) // 2
            m2 = pow(m, 2)
            if m2 < x:
                l = m + 1
            elif m2 > x:
                r = m - 1
            else:
                return m
        return r

    def mySqrt(self, x: int) -> int:
        r = x
        while (r * r > x):
            r = (r + x / r) // 2
        return int(r)

print(Solution().mySqrt(82))
print(Solution().mySqrt(81))
print(Solution().mySqrt(100))
print(Solution().mySqrt(101))
print(Solution().mySqrt(0))