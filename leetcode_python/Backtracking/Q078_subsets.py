from typing import List
import time

class Solution:
    def subsets_backtracking_pop(self, nums: List[int]) -> List[List[int]]:
        res = []
        level_element = []
        def backtracking(start):
            res.append(level_element[:])
            for i in range(start, len(nums)):
                level_element.append(nums[i])
                backtracking(i + 1)
                level_element.pop()
        backtracking(0)
        return res

    def subsets_backtracing_nopop(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = 0
        def backtracking(start, subset):
            nonlocal n
            n += 1
            res.append(subset)
            for i in range(start, len(nums)):
                backtracking(i + 1, subset + [i])
        backtracking(0, [])
        print(n)
        return res

    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = 0
        def backtracking(start, subset):
            nonlocal n
            n += 1
            if start == len(nums):
                res.append(subset)
            if start < len(nums):
                backtracking(start + 1, subset + [start])
                backtracking(start + 1, subset)
        backtracking(0, [])
        print(n)
        return res

    def subsets2(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for num in nums:
            for item in range(len(res)):
                res.append(res[item] + [num])
        return res

    def subsets4(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for num in nums:
            for item in range(len(res)):
                subset = res[item][:]
                subset.append(num)
                res.append(subset)
        return res



start = time.time()
print(Solution().subsets([0,1,2,3,4]))
print('backtracing',time.time()-start)
start = time.time()
print(Solution().subsets_backtracing_nopop([0,1,2,3,4]))
print('iteration',time.time()-start)
