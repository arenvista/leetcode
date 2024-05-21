# @leet start
# Definition for a binary tree node.
from typing import TypeVarTuple
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root: 
            return False
        targetSum -= root.val

        on_leaf = root.left == None and root.right == None

        if on_leaf:
            reached_target: bool = targetSum == 0
            return reached_target
        return self.hasPathSum(root.left, targetSum) or self.hasPathSum(root.right, targetSum)
# @leet end
