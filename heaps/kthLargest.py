# https://leetcode.com/problems/kth-largest-element-in-a-stream/


# Approach: Using Python heapq
# 1. Initialize a heap with the given list of numbers.
# 2. While the length of the heap is greater than k, pop the smallest element from the heap.
# 3. When ADDing a new element, if the length of the heap is less than k, push the element to the heap.
# 4. If the length of the heap is equal to k, push the element to the heap and pop the smallest element.
# 5. Return the smallest element from the heap.

import heapq
from typing import List


class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums
        heapq.heapify(self.nums)
        while len(self.nums) > k:
            heapq.heappop(self.nums)

    def add(self, val: int) -> int:
        if len(self.nums) < self.k:
            heapq.heappush(self.nums, val)
        else:
            heapq.heappushpop(self.nums, val)
        return self.nums[0]
