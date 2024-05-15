from heapq import *
from typing import List

# @leet start
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = [ nums[_] for _ in range(k)] #create the range we want to keep i.e. kth largest, the root value will be the smallest, so if the heap is set to the largest set of values, the root will be the kth largest
        heapify(heap)
        print(heap)
        for i in range(k, len(nums)):
            num = nums[i]
            if num > heap[0]: #if the new value is larger than the smallest value in the heap add it to the heap
                heapreplace(heap, num)
        print(heap)
        return heap[0]
        
# @leet end
