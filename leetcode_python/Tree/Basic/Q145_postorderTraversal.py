from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def postorderTraversal1(self, root: TreeNode) -> List[int]:
        res = []
        stk = []
        stk.append(root)
        pre = None
        while stk:
            top = stk[-1]
            if (top.left is None and top.right is None) or (pre is not None and (top.left == pre or top.right == pre)):
                stk.pop()
                res.append(top.val)
                pre = top
            else:
                root = top
                if root.right != None:
                    stk.append(root.right)
                if root.left != None:
                    stk.append(root.left)
        return res

    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        res, stk = [], [[root, False]]
        while stk:
            top, visited = stk[-1]
            if visited:
                stk.pop()
                res.append(top.val)
            else:
                stk[-1][1] = True
                if top.right:
                    stk.append([top.right, False])
                if top.left:
                    stk.append([top.left, False])
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
print(Solution().postorderTraversal(t1))
print(Solution().postorderTraversal1(t1))