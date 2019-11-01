# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return sum == 0
        record = [[root, root.val]]
        while record:
            tn, s = record.pop(0)
            if not tn.left and not tn.right:
                if s == sum:
                    return True
            if tn.right:
                record.append([tn.right, s + tn.right.val])
            if tn.left:
                record.append([tn.left, s + tn.left.val])
        return False


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
print(Solution().hasPathSum(t1, 16))

print(Solution().hasPathSum(t1, 15))