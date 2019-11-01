from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root:
            left = self.invertTree(root.left)
            right = self.invertTree(root.right)
            root.right = left
            root.left = right
        return root

    def invertTree1(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        stk = [root]
        while stk:
            c = stk.pop()
            tmp = c.left
            c.left = c.right
            c.right = tmp
            if c.left:
                stk.append(c.left)
            if c.right:
                stk.append(c.right)
        return root

    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        res, stk = [], [root]
        while stk:
            new_stk = []
            level_res = []
            while stk:
                nd = stk.pop(0)
                level_res.append(nd.val)
                if nd.left:
                    new_stk.append(nd.left)
                if nd.right:
                    new_stk.append(nd.right)
            res.append(level_res)
            stk = new_stk
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
print(Solution().levelOrder(t1))
t = Solution().invertTree(t1)
print(Solution().levelOrder(t))