# @leet start
# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        node = head
        while node != None:
            if node.val == 'visited':
                return True
            node.val = 'visited'
            node = node.next
        return False
        
# @leet end
