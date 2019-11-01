from typing import List


class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        kl = []
        for i in range(len(nums)):
            l = 0
            r = len(kl) - 1
            while l <= r:
                p = (l + r) // 2
                if nums[i] >= kl[p]:
                    l = p + 1
                else:
                    r = p - 1
            if l != 0 and abs(kl[l - 1] - nums[i]) <= t:
                return True
            if l < len(kl) and abs(kl[l] - nums[i]) <= t:
                return True
            kl.insert(l, nums[i])
            if len(kl) > k:
                kl.remove(nums[i - k])
        return False

print(Solution().containsNearbyAlmostDuplicate([1,2,3,1], 3, 0))
print(Solution().containsNearbyAlmostDuplicate([1,0,1,1], 1, 2))
print(Solution().containsNearbyAlmostDuplicate([1,5,9,1,5,9], 2, 3))
print(Solution().containsNearbyAlmostDuplicate([2,2], 3, 0))
print(Solution().containsNearbyAlmostDuplicate([7,1,3], 2, 3))

print(Solution().containsNearbyAlmostDuplicate([], 0, 0))