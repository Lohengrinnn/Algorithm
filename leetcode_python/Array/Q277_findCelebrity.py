def knows(a, b):
    m = [[1, 1, 0],
         [0, 1, 0],
         [1, 1, 1]]
    return m[a][b] == 1

class Solution(object):
    def findCelebrity(self, n):
        """
        :type n: int
        :rtype: int
        """
        for i in range(n):
            knows_other = False
            for j in range(n):
                if knows(i, j) and i != j:
                    knows_other = True
                    break
            if knows_other:
                continue
            knows_by_everyone = True
            for k in range(n):
                if not knows(k, i):
                    knows_by_everyone = False
            if knows_by_everyone:
                return i
        return -1


print(Solution().findCelebrity(3))
