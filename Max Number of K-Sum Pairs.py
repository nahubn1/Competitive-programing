class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        ptr = len(nums)-1
        res = 0
        while ptr > 0:
            tot = nums[0] + nums[ptr]
            if tot < k:
                nums.pop(0)
            elif tot > k:
                nums.pop(ptr)
            else:
                nums.pop(0)
                ptr -= 1
                nums.pop(ptr)
                res += 1
                
                
            ptr -=1
            
        return res
