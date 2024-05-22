# @leet start
from collections import Counter
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        c = Counter(nums)
        for _ in c.values():
            if _ > 1:
                return True
        return False
        
# @leet end
