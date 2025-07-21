#https://leetcode.com/problems/valid-anagram
#Solution2
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)==len(t):
            for i in t:
                if s.count(i) == t.count(i):
                    continue
                else:
                    return False
            return True
        return False