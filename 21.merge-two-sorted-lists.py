# @leet start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        node_temp = ListNode(0) # dummy node, to return the head of the list
        node_curr = node_temp

        while list1 != None or list2 != None:
            if list1 == None:
                node_curr.next = list2
                list2 = list2.next
                node_curr = node_curr.next
                continue

            if list2 == None:
                node_curr.next = list1
                list1 = list1.next
                node_curr = node_curr.next
                continue

            if list1.val < list2.val:
                node_curr.next = list1
                list1 = list1.next
            else:
                node_curr.next = list2
                list2 = list2.next

            node_curr = node_curr.next

        return node_temp.next
        
      
# @leet end
