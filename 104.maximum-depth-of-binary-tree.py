from typing import Optional
# @leet start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def findDepth(node) -> int:
    if node == None:
        return 0
    else:
        leftDepth = findDepth(node.left)
        rightDepth = findDepth(node.right)
        return max(leftDepth, rightDepth) + 1

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        node = root
        return findDepth(node)
# @leet end
