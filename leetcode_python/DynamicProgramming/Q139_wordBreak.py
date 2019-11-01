from typing import List

class Solution:
    def wordBreak1(self, s: str, wordDict: List[str]) -> bool:
        reachedMemo = [True] + [False] * len(s)
        for i in range(1, len(s) + 1):
            for word in wordDict:
                if s[i - len(word) : i] == word and reachedMemo[i - len(word)]:
                    reachedMemo[i] = True
                    break
        return reachedMemo[-1]

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        def _wordBreak(s: str, wordDict: List[str]) -> bool:
            reachedIndex = [0]
            reachedMemo = [False] * len(s)
            while reachedIndex:
                i = reachedIndex.pop(0)
                for word in wordDict:
                    e = i + len(word)
                    if e > len(s) or reachedMemo[e - 1]:
                        continue
                    if s[i:e] == word:
                        reachedMemo[e - 1] = True
                        if e == len(s):
                            return True
                        reachedIndex.append(e)
            return False
        i = 1
        while i < len(wordDict):
            if _wordBreak(wordDict[i], wordDict[:i]):
                wordDict.pop(i)
            else:
                i += 1
        return _wordBreak(s, wordDict)
import datetime

print(Solution().wordBreak1("applepenapple", ["apple", "pen"]))
print(Solution().wordBreak1("catsandog", ["cats", "dog", "sand", "and", "cat"]))
dt = datetime.datetime.now()
print(Solution().wordBreak1("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab",["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]))
print(datetime.datetime.now() - dt)