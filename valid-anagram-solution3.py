#https://leetcode.com/problems/valid-anagram
#Solution 3
from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)