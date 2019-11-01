import sys
from typing import List


class Solution:
    def shortestDistance(self, words: List[str], word1: str, word2: str) -> int:
        pos1 = -1
        pos2 = -1
        res = sys.maxsize
        for i in range(len(words)):
            if words[i] == word1:
                if pos2 >= 0:
                    res = min(res, i - pos2)
                pos1 = i
            elif words[i] == word2:
                if pos1 >= 0:
                    res = min(res, i - pos1)
                pos2 = i
        return res


print(Solution().shortestDistance(["practice", "makes", "perfect", "coding", "makes"], 'coding', 'practice'))