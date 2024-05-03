# https://leetcode.com/problems/valid-anagram/description/

class SolutionOne:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) == len(t):
            sortedS = sorted(list(s))
            sortedT = sorted(list(t))

            for i in range(len(s)):
                if sortedS[i] != sortedT[i]:
                    return False
            return True
        return False


class SolutionTwo:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) == len(t):
            sorted_s = sorted(list(s))
            sorted_t = sorted(list(t))
            joined_s = "".join(sorted_s)
            joined_t = "".join(sorted_t)

            return joined_s == joined_t
        return False
