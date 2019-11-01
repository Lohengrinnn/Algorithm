from typing import List
from Tree.Basic.TreeNode import *


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        res, queue = [], [root]
        ltor = True
        while queue:
            level_res, level_queue = [], []
            while queue:
                tn = queue.pop(0)
                if ltor:
                    level_res.append(tn.val)
                else:
                    level_res.insert(0, tn.val)
                if tn.left:
                    level_queue.append(tn.left)
                if tn.right:
                    level_queue.append(tn.right)
            ltor = not ltor
            queue = level_queue
            res.append(level_res)
        return res


t1 = TreeNode(1)        #  1
t2 = TreeNode(2)        #   \
t3 = TreeNode(3)        #    2
t4 = TreeNode(4)        #     \
t5 = TreeNode(5)        #      3
t1.right = t2           #     / \
t2.right = t3           #    4   5
t3.left = t4            #   / \  /\
t3.right = t5           #  7  9 6  8
t4.left = TreeNode(7)
t4.right = TreeNode(9)
t5.left = TreeNode(6)
t5.right = TreeNode(8)
print(Solution().zigzagLevelOrder(t1))