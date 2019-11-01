from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        if not root:
            return []
        res = []
        record = [(root, [root.val], root.val)]
        while record:
            tn, trace, s = record.pop()
            if not tn.left and not tn.right:
                if s == sum:
                    res.append(trace)
            if tn.right:
                record.append((tn.right, trace + [tn.right.val], s + tn.right.val))
            if tn.left:
                record.append((tn.left, trace + [tn.left.val], s + tn.left.val))
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
print(Solution().pathSum(t1, 17))
print(Solution().pathSum(t1, 19))
