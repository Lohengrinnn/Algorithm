from typing import List

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stk = [0]
        res = 0
        for c in s:
            if c == '(':
                stk.append(0)
            else:
                if len(stk) == 1:
                    stk[0] = 0
                else:
                    n = stk.pop()
                    stk[-1] += (n + 2)
                    res = max(res, stk[-1])
        return res



print(Solution().longestValidParentheses("()())(()))()(()())"))