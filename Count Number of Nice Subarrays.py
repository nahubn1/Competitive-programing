class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        for i in range(len(nums)):
            nums[i] = 0 if nums[i]%2 == 0 else  1 
        
        tot = 0
        res = 0
        pre_sum = {0:1}
        for i in nums:
            tot += i
            if tot - k in pre_sum:
                res += pre_sum[tot-k]
        
            if tot in pre_sum:
                pre_sum[tot] += 1
            else:
                pre_sum[tot] = 1
            
            
        return res
