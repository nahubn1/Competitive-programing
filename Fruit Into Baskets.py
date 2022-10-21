class Solution:
    def totalFruit(self, nums: List[int]) -> int:
        start = 0
        maxFiruts = 0
        basket1 = []
        basket2 = []
        
        for end in range(len(nums)):
            while (len(basket1) != 0 and nums[end] != basket1[0]) and (len(basket2) != 0 and nums[end] != basket2[0]):
                if nums[start] == basket1[0]:
                    basket1.remove(nums[start])
                else:
                    basket2.remove(nums[start])
                start += 1
                
            if len(basket1) != 0 and nums[end] == basket1[0]:
                basket1.append(nums[end])
            elif len(basket2) != 0 and nums[end] == basket2[0]:
                basket2.append(nums[end])
            else:
                if len(basket1) == 0:
                    basket1.append(nums[end])
                else:
                    basket2.append(nums[end])
        
            maxFiruts = max(maxFiruts, end-start+1)
            
        return maxFiruts
        
