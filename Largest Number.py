class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums.sort(reverse=True)
        nums = [str(i) for i in nums]
        for i, num in enumerate(nums):
            loc = i
            while loc > 0:
                if int(num) > int(nums[loc-1][:len(num)]):
                    loc -= 1
                elif int(num) == int(nums[loc-1][:len(num)]):
                    if int(num+nums[loc-1][len(num):]) > int(nums[loc-1][len(num):]+num):
                        loc -= 1
                    else:
                        break
                else:
                    break
            
            
            nums.pop(i)
            nums.insert(loc, num)
            
        return str(int(''.join(nums)))
