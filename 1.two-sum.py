# @leet start
from typing import List

def solve(nums: List[int], target: int) -> List[int]:
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    raise Exception("No solution")
    
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        return solve(nums, target)

# @leet end
