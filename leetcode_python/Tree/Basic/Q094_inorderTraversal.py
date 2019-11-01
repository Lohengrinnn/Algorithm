from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        c = root
        res = []
        stk = []
        while c is not None or len(stk) != 0:
            while c is not None:
                stk.append(c)
                c = c.left
            if len(stk) != 0:
                l = stk.pop()
                res.append(l.val)
                c = l.right
        return res


    def inorderTraversal1(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        res = []
        stk = [[root, False]]
        while stk:
            c, visited = stk.pop()
            if visited:
                res.append(c.val)
                continue
            if c.right:
                stk.append([c.right, False])
            stk.append([c, True])
            if c.left:
                stk.append([c.left, False])
        return res


t1 = TreeNode(1)        #  1
t2 = TreeNode(2)        #   \
t3 = TreeNode(3)        #    2
t4 = TreeNode(4)        #     \
t5 = TreeNode(5)        #      3
t1.right = t2           #     / \
t2.right = t3           #    4   5
t3.left = t4            #     \   \
t3.right = t5           #      7   6
t5.right = TreeNode(6)
t4.right = TreeNode(7)
print(Solution().inorderTraversal(t1))
print(Solution().inorderTraversal1(t1))

t1 = TreeNode(1)        #  1
t2 = TreeNode(2)        #   \
t3 = TreeNode(3)        #    2
t1.right = t2           #     \
t2.right = t3           #      3
print(Solution().inorderTraversal(t1))
print(Solution().inorderTraversal1(t1))