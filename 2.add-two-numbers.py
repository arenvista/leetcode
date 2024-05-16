# @leet start
# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def construct_num(l: Optional[ListNode]) -> int:
    num = 0
    i = 0
    while l:
        num += l.val * 10**i
        l = l.next
        i += 1
    return num

def construct_list(i: int) -> Optional[ListNode]:
    i = str(i)[::-1]
    head = ListNode(i[0])
    current = head
    for n in i[1:]:
        current.next = ListNode(n)
        current = current.next
    return head


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = construct_num(l1)
        num2 = construct_num(l2)
        num = num1 + num2
        return construct_list(num)
        
# @leet end
