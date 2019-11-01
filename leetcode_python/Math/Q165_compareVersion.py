class Solution:
    def getSubVersion(self, version: str, s: int):
        if s < 0:
            return 0, s
        dot_index = version.find('.', s)
        v = int(version[s:dot_index]) if dot_index > 0 else int(version[s:])
        return v, dot_index + 1 if dot_index > 0 else -1
    def compareVersion(self, version1: str, version2: str) -> int:
        i1 = i2 = 0
        while i1 >= 0 or i2 >= 0:
            v1, i1 = self.getSubVersion(version1, i1)
            v2, i2 = self.getSubVersion(version2, i2)
            if v1 < v2:
                return -1
            elif v1 > v2:
                return 1
        return 0


print(Solution().compareVersion("3.0", "3"))
print(Solution().compareVersion("3.1", "3.1.2"))
print(Solution().compareVersion("0.0.0", "0.0.00"))
