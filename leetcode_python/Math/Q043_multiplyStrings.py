class Solution:
    def add(self, num1: str, num2: str) -> str:
        i1 = len(num1) - 1
        i2 = len(num2) - 1
        carry = 0
        res = ""
        while i1 >= 0 or i2 >= 0 or carry:
            d1 = int(num1[i1]) if i1 >= 0 else 0
            d2 = int(num2[i2]) if i2 >= 0 else 0
            carry, dout = divmod(d1 + d2 + carry, 10)
            res = str(dout) + res
            i1 -= 1
            i2 -= 1
        return res

    def multiply1(self, num1: str, num2: str) -> str:
        if not num1 or not num2 or int(num1) == 0 or int(num2) == 0:
            return "0"
        res = ""
        for i1 in range(len(num1)):
            d1 = int(num1[len(num1) - 1 - i1])
            if d1 == 0:
                continue
            snippet = "0" * i1
            carry = 0
            for i2 in range(len(num2)):
                d2 = int(num2[len(num2) - 1 - i2])
                carry, rem = divmod(d1 * d2 + carry, 10)
                snippet = str(rem) + snippet
            if carry:
                snippet = str(carry) + snippet
            res = self.add(res, snippet)
        return res

    def multiply(self, num1: str, num2: str) -> str:
        if not num1 or not num2 or int(num1) == 0 or int(num2) == 0:
            return "0"
        carry = 0
        res = ""
        len_res = len(num2) + len(num1) - 1
        for i in range(len_res):
            digit = 0
            for i1 in range(len(num1)):
                i2 = i - i1
                if 0 <= i2 < len(num2):
                    d1 = int(num1[len(num1) - 1 - i1])
                    d2 = int(num2[len(num2) - 1 - i2])
                    digit += d1 * d2
            carry, rem = divmod(digit + carry, 10)
            res = str(rem) + res
        if carry:
            res = str(carry) + res
        return res

print(Solution().multiply("523", "21"))
print(Solution().multiply("523", ""))