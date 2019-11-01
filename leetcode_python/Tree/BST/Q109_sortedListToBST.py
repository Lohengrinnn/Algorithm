from Tree.Basic.TreeNode import *


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        len = 0
        ln = head
        while ln:
            len += 1
            ln = ln.next
        def mkTree(start, end):
            nonlocal head
            if start > end:
                return None
            middle = (end + start + 1) // 2
            left = mkTree(start, middle - 1)
            res = TreeNode(head.val)
            head = head.next
            right = mkTree(middle + 1, end)
            res.left = left
            res.right = right
            return res
        return mkTree(0, len - 1)

n1 = ListNode(-10)
n2 = ListNode(-3)
n3 = ListNode(0)
n4 = ListNode(5)
n5 = ListNode(9)
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
print(treeToString(Solution().sortedListToBST(n1)))
print(treeToString(Solution().sortedListToBST(None)))