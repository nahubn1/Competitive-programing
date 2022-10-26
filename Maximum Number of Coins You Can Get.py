class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        n = len(piles)
        steps = int(n/3)
        maxCoins = 0
        i = 1
        while i <= steps:
            maxCoins += piles[n-2*i]
            i += 1
        return maxCoins
            
