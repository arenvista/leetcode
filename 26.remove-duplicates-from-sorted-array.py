# @leet start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        LIST_LENGTH = len(nums)
        unique_nums = 1
        for i in range(1, LIST_LENGTH):
            if nums[i] != nums[i-1]:
                nums[unique_nums] = nums[i]
                unique_nums += 1
        return unique_nums 
# @leet end
