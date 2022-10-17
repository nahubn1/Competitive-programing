class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        res = 0
        prefix_sum = {0:1}
        tot = 0
        for i in nums:
            tot += i
            if tot - k in prefix_sum:
                res += prefix_sum[tot-k]
                
            if tot in prefix_sum:
                prefix_sum[tot] += 1
            else:
                prefix_sum[tot] = 1
            
        return res
