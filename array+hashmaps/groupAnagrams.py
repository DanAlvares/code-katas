# https://leetcode.com/problems/group-anagrams/description/

# Approach:
# 1. Create a key variable and a hashmap.
# 2. Iterate through the list of strings.
# 3. Sort the string and join the sorted string.
# 4. Append the string to the hashmap.
# 5. Return the sorted values of the hashmap.

from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        key = ""
        hashmap = defaultdict(list)
        for string in strs:
            sortedStr = key.join(sorted(string))
            hashmap[sortedStr].append(string)
        return sorted(hashmap.values())