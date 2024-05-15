# @leet start
# Definition for a binary tree node.
from typing import Optional
from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def solution(nums):
    if len(nums) <= 0:
        return
    mid: int = len(nums) // 2 
    print(f"mid {mid}, nums {nums}")
    root = nums[mid]
    left = nums[:mid]
    right = nums[mid+1:]
    return TreeNode(
        val=root, 
        left=solution(left),
        right=solution(right)
    )

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        return solution(nums)
# @leet end
