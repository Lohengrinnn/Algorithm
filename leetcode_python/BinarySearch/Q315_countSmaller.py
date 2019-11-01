from typing import List

class Solution:
    def countSmaller1(self, nums: List[int]) -> List[int]:
        count = []
        def findPosition(target):
            l, r = 0, len(count) - 1
            while l <= r:
                m = l + (r - l) // 2
                if count[m][0] >= target:
                    r = m - 1
                else:
                    l = m + 1
            return l
        res = []
        for i in reversed(nums):
            j = 0
            res_i = 0
            while j < len(count) and count[j][0] < i:
                res_i += count[j][1]
                j += 1
            res.insert(0, res_i)
            index_i = findPosition(i)
            if index_i < len(count) and count[index_i][0] == i:
                count[index_i][1] += 1
            else:
                count.insert(index_i, [i, 1])
        return res


    def countSmaller(self, nums: List[int]) -> List[int]:
        arr, res = [], []
        def findPosition(target):
            l, r = 0, len(arr) - 1
            while l <= r:
                m = l + (r - l) // 2
                if arr[m] >= target:
                    r = m - 1
                else:
                    l = m + 1
            return l
        for i in reversed(nums):
            pos = findPosition(i)
            res.insert(0, pos)
            arr.insert(pos, i)
        return res

print(Solution().countSmaller([5,2,6,1]))