// https://leetcode.com/problems/group-anagrams/description/

function groupAnagrams(strs: string[]): string[][] {
  const stringsMap = new Map<string, string[]>();

  for(const str of strs) {
      const sortedStr = str.split('').sort().join();
      const values = stringsMap.get(sortedStr) || [];

      stringsMap.set(sortedStr, [...values, str]);
  }

  const groups: string[][] = [];
  for(const [key, value] of stringsMap) {
      groups.push(value);
  }

  return groups;
};
