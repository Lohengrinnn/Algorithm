from typing import List

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1 = sorted(nums1)
        nums2 = sorted(nums2)
        def findTargetPosition(l, r, target):
            while l <= r:
                m = l + (r - l) // 2
                if nums1[m] >= target:
                    r = m - 1
                else:
                    l = m + 1
            return l
        l1, l2 = 0, 0
        r1, r2 = len(nums1) - 1, len(nums2) - 1
        res = []
        while l2 <= r2 and l1 <= r1:
            if l2 != 0 and nums2[l2] == nums2[l2 - 1]:
                l2 += 1
                continue
            l1 = findTargetPosition(l1, r1, nums2[l2])
            if l1 < len(nums1) and nums1[l1] == nums2[l2]:
                res.append(nums2[l2])
                l1 += 1
            if nums2[l2] == nums2[r2]:
                break
            l2 += 1
            if r2 != len(nums2) - 1 and nums2[r2] == nums2[r2 + 1]:
                r2 -= 1
                continue
            r1 = findTargetPosition(l1, r1, nums2[r2])
            if r1 < len(nums1) and nums1[r1] == nums2[r2]:
                res.append(nums2[r2])
            r1 -= 1
            r2 -= 1
        return res


print(Solution().intersection([4,4,1,3,5,6], [5,4,4,3,4]))
print(Solution().intersection([1], []))
print(Solution().intersection([], [1]))
print(Solution().intersection([], []))
print(Solution().intersection([4,7,9,7,6,7], [5,0,0,6,1,6,2,2,4, 7]))