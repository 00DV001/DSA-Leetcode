#https://leetcode.com/problems/valid-anagram
#Solution 1
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = sorted(s)
        t = sorted(t)
        if s == t:
            return True
        else:
            return False