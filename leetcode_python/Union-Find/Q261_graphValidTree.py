from typing import List

class TreeNode:
    def __init__(self, v):
        self.val = v
        self.parent = self
        self.rank = 0

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        set = dict()
        map = [None] * n
        for i in range(n):
            map[i] = set[i] = TreeNode(i)
        for j, k in edges:
            def find(x):
                if x.parent != x:
                    x.parent = find(x.parent)
                return x.parent
            def union(x, y):
                set_x = find(x)
                set_y = find(y)
                if set_x != set_y:
                    if set_y.rank > set_x.rank:
                        set_x.parent = set_y
                        set_y.rank += 1
                        del set[set_x.val]
                    else:
                        set_y.parent = set_x
                        set_x.rank += 1
                        del set[set_y.val]
                    return True
                return False
            if not union(map[j], map[k]):
                return False
        return len(set) == 1


print(Solution().validTree(5, [[0,1], [0,2], [0,3], [1,4]]))
print(Solution().validTree(5, [[0,1], [1,2], [2,3], [1,3], [1,4]]))
print(Solution().validTree(5, [[0,1], [1,2], [2,3]]))
print(Solution().validTree(1, []))
print(Solution().validTree(3, [[1, 0]]))
