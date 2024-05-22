# @leet start
# Definition for a Node.
from collections import deque
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def postorder(self, root: Node) -> List[int]:
        stack = deque()
        res = []

        if root == None:
            return res

        stack.appendleft(root) 

        while stack:
            node: Node = stack.popleft() #visit 1st value
            res.append(node.val)
            for child in node.children:
                stack.appendleft(child)

        return res[::-1]
# @leet end
