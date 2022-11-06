class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        i = len(nums) - 1
        while i > 0:
            if nums[i] > nums[i-1]:
                left = nums[:i-1]
                right = sorted(nums[i-1:])
                for j in right:
                    if j > nums[i-1]:
                        minGreater = [j]
                        right.remove(j)
                        break
                        
                nums.clear()
                nums += left + minGreater + right
                break
            else:
                i -= 1
        else:
            nums.reverse()
