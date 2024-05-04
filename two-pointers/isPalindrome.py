# https://leetcode.com/problems/valid-palindrome/

# Approach One: Using Python string manipulation
# 1. Remove all non-alphanumeric characters and convert the string to lowercase.
# 2. Compare the string with its reverse. If they are equal, return True, else False.


class SolutionOne:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(e for e in s if e.isalnum()).lower()
        return s == s[::-1]


# Approach Two: Two pointers
# 1. Remove non-alphanumeric characters and convert the string to lowercase.
# 2. Use two pointers, one at the start and one at the end of the string.
# 3. Compare the characters at the two pointers.
# 4. If they are equal, move the pointers towards each other.
# 5. If they are not equal, return false.
# 6. If the pointers meet, return true.

from typing import List
import re


class SolutionTwo:
    def isPalindrome(self, s: str) -> bool:
        string = re.sub(r"[^0-9a-z]", "", s, flags=re.I).lower()
        left = 0
        right = len(s) - 1

        while left < right:
            if string[left] == string[right]:
                left += 1
                right -= 1
            else:
                return False

        return True
