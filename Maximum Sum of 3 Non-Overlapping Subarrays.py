class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        subSums = [sum(nums[:k])]
        for i in range(1, len(nums)-k+1):
            subSums.append(subSums[-1]-nums[i-1]+nums[i+k-1])
        n = len(subSums)
        
        left, best = [0]*n, 0
        for i in range(n):
            if subSums[i] > subSums[best]:
                best = i
            left[i] = best
        
        right, best = [subSums[-1]]*n, n-1
        for f in range(n-1, -1, -1):
            if subSums[f] >= subSums[best]:
                best = f
            right[f] = best

        maxSum = None
        for m in range(k, n-k):
            i, f = left[m-k], right[m+k]
            Sum = sum([subSums[i], subSums[m], subSums[f]])
            if maxSum is None or Sum > maxSum[1]:
                maxSum = ((i, m, f), Sum)
        
        return maxSum[0]
