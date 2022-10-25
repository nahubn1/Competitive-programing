class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        diff = []
        for i in range(len(nums)-1):
            diff.append(nums[i+1]-nums[i])
        
        postSum = [0]
        for i in reversed(diff):
            postSum.append(postSum[-1]+i)
        
        postSum = list(reversed(postSum))
        winLen = 1
        maxLen = 1
        cost = 0
        start = 0
        for end in range(1, len(nums)):
            cost += (winLen * diff[end-1])
            winLen += 1
            while cost > k:
                cost -= (postSum[start] - postSum[end])
                start += 1
                winLen -= 1
            maxLen = max(maxLen, winLen)
        return maxLen
