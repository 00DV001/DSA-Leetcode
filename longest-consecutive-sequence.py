class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        elif len(nums)==1:
            return 1
        nums = set(nums)
        count = 0
        for i in nums:
            if i-1 not in nums:
                temp = 1
                j = i+1
                while j in nums:
                    temp += 1
                    j += 1
                count = max(count,temp)
        return count