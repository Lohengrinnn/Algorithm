class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bull = 0
        cow = 0
        s = list(secret)
        g = list(guess)
        for i in range(len(s) - 1, -1, -1):
            if s[i] == g[i]:
                bull += 1
                del s[i]
                del g[i]
        for i in range(len(s) - 1, -1, -1):
            if s[i] in g:
                g.remove(s[i])
                cow += 1
        return '%dA%dB'%(bull, cow)

print(Solution().getHint('1123', '0111'))
print(Solution().getHint('1807', '7810'))
print(Solution().getHint('', ''))
print(Solution().getHint('', ''))
