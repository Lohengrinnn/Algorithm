from typing import List

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums2) < len(nums1):
            nums1, nums2 = nums2, nums1
        nums1_dict = {}
        for i in nums1:
            nums1_dict[i] = nums1_dict.get(i, 0) + 1
        res = []
        for j in nums2:
            n = nums1_dict.get(j, 0)
            if n != 0:
                nums1_dict[j] = n - 1
                res.append(j)
        return res

print(Solution().intersect([1,2,2,2,2,2], [1,1,2,2]))