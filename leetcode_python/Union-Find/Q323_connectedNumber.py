from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.p = self
        self.rank = 0


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        sets = dict()
        nmap = [None] * n
        for i in range(n):
            nmap[i] = sets[i] = TreeNode(i)

        def find(x) -> TreeNode:
            if x.p != x:
                x.p = find(x.p)
            return x.p

        def union(x, y):
            x_set = find(x)
            y_set = find(y)
            if x_set != y_set:
                if x_set.rank < y_set.rank:
                    x_set.p = y_set
                    y_set.rank += 1
                    del sets[x_set.val]
                else:
                    y_set.p = x_set
                    x_set.rank += 1
                    del sets[y_set.val]

        for x, y in edges:
            union(nmap[x], nmap[y])
        return len(sets)

    def countComponents1(self, n: int, edges: List[List[int]]) -> int:
        sets = {i: [i] for i in range(n)}

        def find(x):
            for k, v in sets.items():
                if x in v:
                    return k

        def union(x, y):
            kx_set = find(x)
            ky_set = find(y)
            if kx_set != ky_set:
                sets[kx_set] += sets[ky_set]
                del sets[ky_set]
        for x, y in edges:
            union(x, y)
        return len(sets)


print(Solution().countComponents(5, [[0, 1], [1, 2], [3, 4]]))
print(Solution().countComponents(5, [[0, 1], [1, 2], [2, 3], [3, 4]]))
print(Solution().countComponents(0, []))
print(Solution().countComponents(5, [[2, 3]]))