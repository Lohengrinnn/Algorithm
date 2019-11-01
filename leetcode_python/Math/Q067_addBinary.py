class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        ia = len(a) - 1
        ib = len(b) - 1
        res = ""
        while ia >= 0 or ib >= 0 or carry:
            va = int(a[ia]) if ia >= 0 else 0
            vb = int(b[ib]) if ib >= 0 else 0
            sum = va + vb + carry
            carry = 1 if sum >= 2 else 0
            res = str(sum % 2) + res
            ia -= 1
            ib -= 1
        return res


print(Solution().addBinary("111", "111"))
print(Solution().addBinary("111", ""))
print(Solution().addBinary("111", "0"))
print(Solution().addBinary("110", "1"))