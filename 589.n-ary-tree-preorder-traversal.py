# @leet start
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def preorder(self, root: Node) -> List[int]:
        path = []
        return self.walk(root, path)

    def walk(self, node: Node, path: List) -> List[int]:
        if not node:
            return path
        path.append(node.val)
        for child in node.children:
            self.walk(child, path)
        return path

        
# @leet end
