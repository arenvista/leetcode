# @leet start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        path = []
        return self.walk(root, path)

    def walk(self, root: Optional[TreeNode], path=[]) -> List[int]:
        if not root:
            return path
        if root.left != None:
            self.walk(root.left, path)
        path.append(root.val)
        if root.right != None:
            self.walk(root.right, path)
        return path
# @leet end
