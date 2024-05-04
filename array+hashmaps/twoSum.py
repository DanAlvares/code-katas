# https://leetcode.com/problems/two-sum/description/

# Approach:
# 1. Create a hashmap to store the indices of the elements.
# 2. Iterate through the list of numbers.
# 3. Find the difference between the target and the number.
# 4. If the difference is in the hashmap, return the indices of the difference and the current number.
# 5. Else, add the number to the hashmap.
# 6. Return an empty list if no solution is found.

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        memo = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in memo:
                return [memo[diff], i]
            memo[num] = i
        return []