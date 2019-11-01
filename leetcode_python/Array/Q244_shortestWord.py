import sys
from typing import List


class WordDistance:

    def __init__(self, words: List[str]):
        self.d = {}
        for i in range(len(words)):
            l = self.d.get(words[i], [])
            l.append(i)
            self.d[words[i]] = l

    def shortest1(self, word1: str, word2: str) -> int:
        p1 = self.d[word1]
        p2 = self.d[word2]
        res = sys.maxsize
        for i in p2:
            l1, r1 = 0, len(p1) - 1
            while l1 + 1 < r1:
                m = (l1 + r1) // 2
                if p1[m] < i:
                    l1 = m
                else:
                    r1 = m
            res = min(res, abs(p1[l1] - i), abs(p1[r1] - i))
        return res

    def shortest(self, word1: str, word2: str) -> int:
        p1 = self.d[word1]
        p2 = self.d[word2]
        res = sys.maxsize
        s1, s2, r1, r2 = 0, 0, len(p1) - 1, len(p2) - 1
        while s1 <= r1 and s2 <= r2:
            res = min(res, abs(p1[s1] - p2[s2]))
            if p1[s1] > p2[s2]:
                s2 += 1
            else:
                s1 += 1
        return res

words = ["practice", "makes", "perfect", "coding", "makes"]



# Your WordDistance object will be instantiated and called as such:
obj = WordDistance(words)
param_1 = obj.shortest("coding", "makes")
param_1 = obj.shortest("coding", "practice")
print(param_1)