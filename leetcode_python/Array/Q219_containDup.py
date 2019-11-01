from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        d = dict()
        for i in range(len(nums)):
            if nums[i] in d and i - d[nums[i]] <= k:
                return True
            d[nums[i]] = i
        return False

print(Solution().containsNearbyDuplicate([1,2,1], 2))
print(Solution().containsNearbyDuplicate([1,2,1], 1))