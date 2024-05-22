# @leet start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        seen = []
        node = head
        while node != None:
            seen.append(node.val)
            node = node.next
        mid = len(seen) // 2
        if len(seen) % 2 != 0:
            left = seen[:mid]
            right = seen[mid+1:]
        else:
            left = seen[:mid]
            right = seen[mid:]
        if len(seen) == 1:
            return True

        return left == right[::-1]
# @leet end
