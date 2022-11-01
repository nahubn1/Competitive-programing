class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        h_ind = 0
        for i in range(len(citations)):
            if citations[i] >= i+1:
                h_ind = i+1
        return h_ind
