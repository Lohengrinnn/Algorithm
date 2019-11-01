# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSameNode(self, x, y):
        if x and y:
            return x.val == y.val
        elif not x and not y:
            return True
        return False

    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        left_queue, right_queue = [root], [root]
        while left_queue:
            l = left_queue.pop(0)
            r = right_queue.pop(0)
            if not self.isSameNode(l.left, r.right):
                return False
            if l.left:
                left_queue.append(l.left)
                right_queue.append(r.right)
            if not self.isSameNode(l.right, r.left):
                return False
            if l.right:
                left_queue.append(l.right)
                right_queue.append(r.left)
        return True


t1 = TreeNode(1)        #      1
tl2 = TreeNode(2)       #     / \
tr2 = TreeNode(2)       #    2   2
tl3 = TreeNode(3)       #   / \ / \
tr3 = TreeNode(3)       #  3  4 4 3
tl4 = TreeNode(4)       #
tr4 = TreeNode(4)       #
t1.left = tl2
t1.right = tr2
tl2.left = tl3
tl2.right = tl4
tr2.left = tr4
tr2.right = tr3
print(Solution().isSymmetric(t1))
print(Solution().isSymmetric(tl2))
