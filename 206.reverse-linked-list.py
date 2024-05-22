# @leet start
# Definition for singly-linked list.
from collections import deque
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None

        q = deque()
        node = head
        while node != None:
            q.appendleft(node.val)
            node = node.next

        ll_new = ListNode(q.popleft())
        node = ll_new
        while q:
            node.next = ListNode(q.popleft())
            node = node.next
        return ll_new
# @leet end
