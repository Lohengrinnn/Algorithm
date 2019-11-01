class Solution:
    def firstUniqChar(self, s: str) -> int:
        dict_s = {}
        for c in s:
            dict_s[c] = dict_s.get(c, 0) + 1
        for i, c in enumerate(s):
            if dict_s[c] == 1:
                return i
        return - 1


print(Solution().firstUniqChar("leetcode"))
print(Solution().firstUniqChar("leetcodeleetcode"))