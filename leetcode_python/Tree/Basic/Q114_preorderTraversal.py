from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        c = root
        res = []
        stk = []
        while c is not None or len(stk) != 0:
            while c is not None:
                res.append(c.val)
                stk.append(c)
                c = c.left
            if len(stk) != 0:
                c = stk.pop()
                c = c.right
        return res

    def preorderTraversal1(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        res, stk = [], [root]
        while stk:
            c = stk.pop()
            res.append(c.val)
            if c.right:
                stk.append(c.right)
            if c.left:
                stk.append(c.left)
        return res


t1 = TreeNode(1)        #  1
t2 = TreeNode(2)        #   \
t3 = TreeNode(3)        #    2
t4 = TreeNode(4)        #     \
t5 = TreeNode(5)        #      3
t1.right = t2           #     / \
t2.right = t3           #    4   5
t3.left = t4            #   / \  /\
t3.right = t5           #  6  7 8  9
t5.left = TreeNode(8)
t5.right = TreeNode(9)
t4.left = TreeNode(6)
t4.right = TreeNode(7)
print(Solution().preorderTraversal(t1))
print(Solution().preorderTraversal1(t1))

t1 = TreeNode(1)        #      1
t2 = TreeNode(2)        #     / \
t3 = TreeNode(3)        #    4  3
t4 = TreeNode(4)        #   /
t1.right = t3           #  2
t1.left = t4
t4.left = t2
print(Solution().preorderTraversal(t1))
print(Solution().preorderTraversal1(t1))

print(Solution().preorderTraversal(None))
print(Solution().preorderTraversal1(None))
