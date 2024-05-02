class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        key = ""
        hashmap = defaultdict(list)
        for string in strs:
            sortedStr = key.join(sorted(string))
            hashmap[sortedStr].append(string)
        return sorted(hashmap.values())