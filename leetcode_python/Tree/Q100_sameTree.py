# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSameNode(self, p, q):
        if p and q:
            return p.val == q.val
        elif not p and not q:
            return True
        return False

    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not self.isSameNode(p, q):
            return False
        elif not p:
            return True
        q_p, q_q = [p], [q]
        while q_p:
            p = q_p.pop(0)
            q = q_q.pop(0)
            if not self.isSameNode(p.left, q.left) or not self.isSameNode(p.right, q.right):
                return False
            if p.left:
                q_p.append(p.left)
                q_q.append(q.left)
            if p.right:
                q_p.append(p.right)
                q_q.append(q.right)
        return True


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
print(Solution().isSameTree(t1, t1))
print(Solution().isSameTree(None, None))
