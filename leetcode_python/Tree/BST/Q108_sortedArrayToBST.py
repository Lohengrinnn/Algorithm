from Tree.Basic.TreeNode import TreeNode
from Tree.Basic.TreeNode import stringToTreeNode
from Tree.Basic.TreeNode import treeToString
from typing import List

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None
        left = 0
        right = len(nums) - 1
        middle = len(nums) // 2
        root = TreeNode(nums[middle])
        if left <= middle - 1:
            root.left = self.sortedArrayToBST(nums[left : middle])
        if right >= middle + 1:
            root.right = self.sortedArrayToBST(nums[middle + 1 : right + 1])
        return root

print(treeToString(stringToTreeNode('[0,-3,9,-10,null,5]')))
print(treeToString(Solution().sortedArrayToBST([-10,-3,0,5,9])))


