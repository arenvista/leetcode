# @leet start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        node = head
        while node != None:
            if node.val == "seen":
                return True
            node.val = "seen"
            node = node.next

# @leet end
