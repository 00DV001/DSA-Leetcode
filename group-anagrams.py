#https://leetcode.com/problems/group-anagrams
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        L1 = strs
        L2 = []
        for i in L1:
            L2.append(''.join(sorted(i)))
        Dict1 = {}
        for j_og,k_sorted in zip(L1, L2):
            if k_sorted not in Dict1:
                Dict1[k_sorted] = []
            Dict1[k_sorted].append(j_og)
        result  = list(Dict1.values())
        return result