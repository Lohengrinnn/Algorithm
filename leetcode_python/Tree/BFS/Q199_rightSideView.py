from typing import List
from Tree.Basic.TreeNode import *


class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        res, queue = [], [root]
        while queue:
            res.append(queue[-1].val)
            level_queue = []
            while queue:
                tn = queue.pop(0)
                for n in (tn.left, tn.right):
                    if n:
                        level_queue.append(n)
            queue = level_queue
        return res


t1 = TreeNode(1)        #  1
t2 = TreeNode(2)        #   \
t3 = TreeNode(3)        #    2
t4 = TreeNode(4)        #     \
t5 = TreeNode(5)        #      3
t1.right = t2           #     / \
t2.right = t3           #    4   5
t3.left = t4            #   / \
t3.right = t5           #  7  9
t4.left = TreeNode(7)
#t4.right = TreeNode(9)
print(Solution().rightSideView(t1))
