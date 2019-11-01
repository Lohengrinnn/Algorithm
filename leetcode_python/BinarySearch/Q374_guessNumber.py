def guess(num):
    if num > 6:
        return -1
    elif num < 6:
        return 1
    else:
        return 0


class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        l = 1
        r = n
        while l <= r:
            m = l + (r - l) // 2
            if guess(m) < 0:
                r = m - 1
            elif guess(m) > 0:
                l = m + 1
            else:
                return m

for i in range(6, 11):
    print(Solution().guessNumber(i))
