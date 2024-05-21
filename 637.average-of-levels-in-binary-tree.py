# @leet start
# Definition for a binary tree node.
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        res = []
        q = deque()
        q.append(root)
        level_sum = 0
        while(q): 
            level_sum = 0
            q_size = len(q)
            for _ in range(0,q_size):
                node_curr = q.popleft()
                level_sum += node_curr.val
                if node_curr.left != None:
                    q.append(node_curr.left)
                if node_curr.right != None:
                    q.append(node_curr.right)
            level_avg = level_sum / q_size
            res.append(level_avg)
        return res
# @leet end
