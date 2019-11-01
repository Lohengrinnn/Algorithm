class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.rstrip(' ')
        end = len(s)
        space_index = s.rfind(' ')
        if space_index >= 0:
            return end - space_index - 1
        else:
            return end

print(Solution().lengthOfLastWord(''))
print(Solution().lengthOfLastWord(' '))
print(Solution().lengthOfLastWord('      '))
print(Solution().lengthOfLastWord('hello   '))
print(Solution().lengthOfLastWord('hello'))
print(Solution().lengthOfLastWord('hello world'))