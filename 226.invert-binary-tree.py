# @leet start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        
        child_left = self.invertTree(root.left)
        child_right = self.invertTree(root.right)


        #swap the children
        root.right = child_left
        root.left = child_right

        return root
# @leet end
