# @leet start
from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        jumps = 0
        breadth_end = 0
        dist_max = 0
        for fuel in range(len(nums)):
            # Find the distance you can travel initially (current level/breadth)
            # In this range is there any point that you can take that will take you further than the current end point (next level/depth)
            dist_f_new = fuel + nums[fuel] # at this index we could go this far if we refueled
            dist_max = max(dist_max, dist_f_new) # given the options, the furthest we could go
            # If we reach the end point, return the number of jumps
            if dist_max >=  len(nums) - 1:
                jumps += 1
                return jumps
            if fuel == breadth_end:
                # If we reach the end of the current breadth, update the breadth end point
                jumps += 1
                breadth_end = dist_max
            # If so, update the end point to that point
        return jumps

# @leet end
