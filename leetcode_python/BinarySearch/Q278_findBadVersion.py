def isBadVersion(version):
    if version >= 5:
        return True
class Solution:
    def firstBadVersion(self, n):
        l = 1
        r = n
        while l <= r:
            m = l + (r - l) // 2
            if isBadVersion(m):
                r = m - 1
            else:
                l = m + 1
        return l

print(Solution().firstBadVersion(10))