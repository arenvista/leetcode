# @leet start
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        #add it all togther then sort in place
        for i in range(n):
            nums1[m+i] = nums2[i]
        nums1.sort()
# @leet end
