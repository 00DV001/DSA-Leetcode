#https://leetcode.com/problems/missing-number
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        NSum = n*(n+1)//2
        LSum = sum(nums)
        return NSum - LSum