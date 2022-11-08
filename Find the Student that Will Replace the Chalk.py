class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        preSum = [chalk[0]]
        for i in range(1, len(chalk)):
            preSum.append(preSum[-1]+chalk[i])
        rem = k%preSum[-1]
        for i in range(len(preSum)):
            if preSum[i] > rem:
                return i
