from typing import List
import sys

class Solution:
    def jump(self, nums: List[int]) -> int:
        if not nums or len(nums) == 1:
            return 0
        step = 0
        cur = 0
        while True:
            if cur + nums[cur] >= len(nums) - 1:
                return step + 1
            for i in range(cur, cur + nums[cur] + 1):
                if i + nums[i] > cur + nums[cur]:
                    cur = i
            step += 1



print(Solution().jump([2,3,1,1,0]))
print(Solution().jump([0]))
l = []
for i in range(25000, 0, -1):
    l.append(i)
l.append(1)
l.append(1)
l.append(0)
print(len(l))
print(Solution().jump(l))
