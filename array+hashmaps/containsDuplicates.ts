// https://leetcode.com/problems/contains-duplicate/description/

function containsDuplicate(nums: number[]): boolean {
  const uniqueNums = new Set<number>(nums);
  return nums.length > uniqueNums.size;
};