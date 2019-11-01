from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        for i in range(len(digits) - 1, -1, -1):
            digits[i] += 1
            if digits[i] == 10:
                digits[i] = 0
            else:
                carry = 0
                break
        if carry:
            digits.insert(0, 1)
        return digits

print(Solution().plusOne([1,2,3,4]))
print(Solution().plusOne([0,2,3]))
print(Solution().plusOne([9]))
