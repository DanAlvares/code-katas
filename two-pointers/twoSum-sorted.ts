// https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/

// Approach:
// 1. Initialize two pointers, start and end.
// 2. While start is less than the length of the array, do the following:
// 3. Calculate the sum of the elements at start and end.
// 4. If the sum is less than the target, increment start.
// 5. If the sum is greater than the target, decrement end.
// 6. If the sum is equal to the target, return the indices of the elements.

function twoSum(numbers: number[], target: number): number[] {
  let start = 0;
  let end = numbers.length - 1;

  while (start < end) {
    const sum = numbers[start] + numbers[end];

    if (sum === target) {
      return [start + 1, end + 1];
    }

    if (sum < target) {
      start++;
    } else {
      end--;
    }
  }

  return [start + 1, end + 1];
}
