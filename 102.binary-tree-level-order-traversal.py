# @leet start
# Definition for a binary tree node.
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque()
        q.append(root)
        res = []
        if root == None:
            return []

        if root.left == None and root.right == None:
            x = [root.val]
            return [x]

        while q:
            level = []
            for _ in range(len(q)):
                curr_node = q.popleft()
                if curr_node.left != None:
                    q.append(curr_node.left)
                if curr_node.right != None:
                    q.append(curr_node.right)
                level.append( curr_node.val )
            res.append(level)
        return res


        
# @leet end
