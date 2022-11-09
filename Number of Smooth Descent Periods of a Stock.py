class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        stack, i = [], 0
        while i < len(prices):
            winLen = 1
            while i < len(prices)-1 and prices[i]-prices[i+1] == 1:
                winLen += 1
                i += 1
            i += 1
            stack.append(winLen)
        return int(sum([(n)*(n+1)/2 for n in stack]))
