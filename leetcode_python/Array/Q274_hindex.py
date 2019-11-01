from typing import List


class Solution:
    def hIndex1(self, citations: List[int]) -> int:
        citations = sorted(citations, reverse=True)
        p = 0
        r = len(citations) - 1
        while True:
            if p > r:
                return 0
            i = (p + r) // 2
            if citations[i] == i + 1:
                return i + 1
            # if cit[i + 1] >= i + 2, than i + 2 will be available answer
            elif citations[i] > i + 1 and (i == len(citations) - 1 or citations[i + 1] < i + 2):
                return i + 1
            elif citations[i] > i + 1:
                p = i + 1
            elif citations[i] < i + 1:
                r = i - 1


    def hIndex2(self, citations):
        n = len(citations)
        cita_num = [0] * n
        for c in citations:
            if c >= n:
                cita_num[n - 1] += 1
            elif c > 0:
                cita_num[c - 1] += 1

        for i in range(n - 2, -1, -1):
            if i + 2 <= cita_num[i + 1]:
                return i + 2
            cita_num[i] += cita_num[i + 1]
        if len(cita_num) > 0 and cita_num[0] > 0:
            return 1
        else:
            return 0


    def hIndex(self, citations):
        n = len(citations)
        cita_num = [0] * (n + 1)
        for c in citations:
            if c >= n:
                cita_num[n] += 1
            elif c > 0:
                cita_num[c] += 1

        for i in range(n - 1, -1, -1):
            if i + 1 <= cita_num[i + 1]:
                return i + 1
            cita_num[i] += cita_num[i + 1]
        return 0

print(Solution().hIndex([3,0,6,1,5]))
print(Solution().hIndex([3,0,6,1,5,5,5,5]))
print(Solution().hIndex([3,0,6,1,5,5,5,5, 5]))
print(Solution().hIndex([]))
print(Solution().hIndex([0]))
print(Solution().hIndex([1, 1]))
