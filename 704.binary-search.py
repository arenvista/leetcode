# @leet start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return -1
        lb = 0
        up = len(nums)-1 

        while lb <= up:
            mid = lb + (up-lb) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] < target: #if the value is less than our target; we need larger numbers -> search right
                lb = mid+1
            elif nums[mid] > target:
                up = mid-1
        return -1

# @leet end
