# @leet start
from typing import List
def solve(nums, target, lo, hi):
    mid = (lo + hi) // 2
    print(lo, mid, hi)
    if mid == lo:
        if target > nums[mid]:
            return hi 
        else:
            return lo

    if nums[mid] == target:
        return mid

    elif nums[mid] < target: #if the middle value is less than our target, we search the larger range
        print('searching right')
        return solve(nums, target, mid, hi)

    elif nums[mid] > target: #if the middle value is less than our target, we search the smaller range
        print('searching left')
        return solve(nums, target, lo, mid)

class Solution:
    def searchInsert(self, nums: List[int], target: int):
        print(f'searching for {target} in {nums}')
        n = len(nums)
        return solve(nums, target, 0, n)

input = [1,3,5,6]
target = 5
# @leet end

