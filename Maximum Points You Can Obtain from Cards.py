class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        currScore, s, e = sum(cardPoints[:k]), -1, k-2
        maxScore = currScore
        # print(currScore)
        while e >= -1:
            currScore += (cardPoints[s] - cardPoints[e+1])
            # print(s, e, currScore)
            maxScore = max(maxScore, currScore)
            s, e = s-1, e-1
        return maxScore
