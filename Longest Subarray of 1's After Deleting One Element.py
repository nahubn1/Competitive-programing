class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        if 0 not in nums:
            return len(nums)-1
        zeroCount, oneCount, maxCount, s = 0, 0, 0, 0
        for e in range(len(nums)):
            if nums[e] == 0:
                zeroCount += 1
            else:
                oneCount += 1
            while zeroCount > 1:
                if nums[s] == 0:
                    zeroCount -= 1
                else:
                    oneCount -= 1
                s += 1
                
            maxCount  = max(maxCount, oneCount)
            
        return maxCount
