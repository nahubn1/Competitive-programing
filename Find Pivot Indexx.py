class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        right = sum(nums)
        left = 0
        last_mass = 0
        
        for i in range(len(nums)):
                
            right -= nums[i]
            left += last_mass
            
            
            if left == right:
                return i
            
            last_mass = nums[i]
            
        return -1
