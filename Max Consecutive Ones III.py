class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        
        start  = 0
        end = 0
        
        zeros_pre_sum = [0]
        count = 0
        for i in nums:
            if i == 0:
                count += 1
            zeros_pre_sum.append(count)
        zeros_pre_sum.append(zeros_pre_sum[-1])
        
        max_len = 0
        while start <= end < len(nums):
            # zeros count the number of zeros that will exist if we expand our window
            zeros =  zeros_pre_sum[end+1] - zeros_pre_sum[start]
            # print('s =', start, 'e =', end, 'z =', zeros)
            if zeros <= k:
                #expand
                end+=1
            else:
                if start != end:
                    #contract
                    start+=1
                else:
                    #skip
                    start+=1
                    end+=1
            
            max_len = max(max_len, end-start)
            
        return max_len
            
        
        
        return length
