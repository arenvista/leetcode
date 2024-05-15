# @leet start
# Definition for a binary tree node.
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def findDepth(node) -> int:
    if node == None: #if we are off the tree, don't count, end this cycle
        return 0
    ld = findDepth(node.left)
    rd = findDepth(node.right)
    if node.left == node.right == None: #if we are on a leaf node, count the node end the cycle
        return 1
    if node.left == None and node.right != None: # if we cant go left; go right
        return rd + 1
    if node.right == None and node.left != None: # if we cant go right; go left
        return ld + 1
    return min(ld, rd) + 1 # of the all paths in from the starting node; return the shortest path to a leaf

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        return findDepth(root)
# @leet end
