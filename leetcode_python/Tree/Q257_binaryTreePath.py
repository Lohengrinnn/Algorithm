from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def binaryTreePaths2(self, root: TreeNode) -> List[str]:
        if not root:
            return []
        res, stk = [], [[root, False]]
        path = ''
        while stk:
            c, visited = stk[-1]
            if visited:
                path = path[:path.rfind('->')]
                stk.pop()
                continue
            stk[-1][1] = True
            if not path:
                path = '%d' % c.val
            else:
                path += '->%d' % c.val
            if c.right:
                stk.append([c.right, False])
            if c.left:
                stk.append([c.left, False])
            if not c.left and not c.right:
                res.append(path)
        return res


    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root:
            return []
        if not root.left and not root.right:
            return ['%d' % root.val]
        res = []
        cur = '%d->' % root.val
        if root.left:
            res_l = self.binaryTreePaths(root.left)
            res += [cur + s for s in res_l]
        if root.right:
            res_r = self.binaryTreePaths(root.right)
            res += [cur + s for s in res_r]
        return res

    def binaryTreePaths1(self, root: TreeNode) -> List[str]:
        if not root:
            return []
        res = []
        record = [[root, '%d' % root.val]]
        while record:
            c, str = record.pop()
            if not c.right and not c.left:
                res.append((str))
            if c.right:
                record.append([c.right, str + '->%d' % c.right.val])
            if c.left:
                record.append([c.left, str + '->%d' % c.left.val])
        return res
# 如果使用BFS, 并不是xian

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
print(Solution().binaryTreePaths(t1))
print(Solution().binaryTreePaths1(t1))

t1 = TreeNode(37)       #      37
t2 = TreeNode(-34)      #   -34  -48
t3 = TreeNode(-48)      #    -100
t4 = TreeNode(-100)
t5 = TreeNode(5)
t1.left = t2
t1.right = t3
t2.right = t4
print(Solution().binaryTreePaths(t1))
print(Solution().binaryTreePaths1(t1))
print(Solution().binaryTreePaths1(None))