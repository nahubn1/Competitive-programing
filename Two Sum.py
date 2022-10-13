class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lo = 0
        hi = len(nums)-1
        nums = sorted(enumerate(nums), key=lambda item: item[1])
        while True:
            # print(lo, hi)
            tot = nums[lo][1] + nums[hi][1]
            if tot > target:
                hi -= 1
            elif tot < target:
                lo += 1
            else:
                return nums[lo][0], nums[hi][0]
