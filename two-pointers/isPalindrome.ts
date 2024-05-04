// https://leetcode.com/problems/valid-palindrome/

// Approach: Two pointers
// 1. Remove non-alphanumeric characters and convert the string to lowercase.
// 2. Use two pointers, one at the start and one at the end of the string.
// 3. Compare the characters at the two pointers.
// 4. If they are equal, move the pointers towards each other.
// 5. If they are not equal, return false.
// 6. If the pointers meet, return true.

function isPalindrome(s: string): boolean {
  const string = s.replace(/[^0-9a-z]/gi, '').toLowerCase();

  let left = 0;
  let right = string.length - 1;

  while (left < right) {
    if (string[left] === string[right]) {
      left++;
      right--;
    } else {
      return false;
    }
  }

  return true;
}

// Using built-in functions
function isPalindromeNative(s: string): boolean {
  const alphaStr = s.replace(/[^0-9a-z]/gi, '').toLowerCase();
  const reversed = alphaStr.split('').reverse().join('');

  return alphaStr === reversed;
}
