# @leet start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def validateBST(self, node, low, high) -> bool:
        if not node:
            return True
        if low >= node.val or high <= node.val: 
            return False
        return self.validateBST(node.left, low, node.val) and self.validateBST(node.right, node.val, high)

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.validateBST(root, float('-inf'), float('inf'))
# @leet end
