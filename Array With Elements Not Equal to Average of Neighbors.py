class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)
        result = []
        if n%2 == 0:
            for i in range(int(n/2)):
                result.append(nums[i])
                result.append(nums[n-1-i])
        else:
            for i in range(int((n-1)/2)):
                result.append(nums[i])
                result.append(nums[n-1-i])
            result.append(nums[int((n-1)/2)])
                
        return result
