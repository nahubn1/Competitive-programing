from math import inf
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = -inf
        Sum = 0
        for num in nums:
            Sum += num
            maxSum = max(maxSum, Sum)
            if Sum < 0: Sum = 0
        return maxSum
