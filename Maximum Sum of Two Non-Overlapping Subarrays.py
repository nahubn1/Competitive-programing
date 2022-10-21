class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        totalMaxSum = 0
        for back, front in ((firstLen, secondLen), (secondLen, firstLen)):
            
            maxSumBeforeJ = [sum(nums[: back])]
            for j in range(1, len(nums)-front-back+1):
                maxSumBeforeJ.append(max(maxSumBeforeJ[-1], sum(nums[j:j+back])))
            
            maxSumAfterJ = [sum(nums[len(nums)-front: len(nums)])]
            for j in range(len(nums)-front-1, back-1, -1):
                maxSumAfterJ.append(max(maxSumAfterJ[-1], sum(nums[j: j+front])))
            
            maxSumAtJ = []
            for j in range(len(maxSumBeforeJ)):
                maxSumAtJ.append(maxSumBeforeJ[j] + maxSumAfterJ[-(j+1)])
            
            totalMaxSum = max(totalMaxSum, max(maxSumAtJ))
            
        return totalMaxSum
