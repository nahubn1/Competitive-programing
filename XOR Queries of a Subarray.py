class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        preXOR = [0]
        for i in arr:
            preXOR.append(preXOR[-1]^i)
        output  =[]
        for s, e in queries:
            output.append(preXOR[s]^preXOR[e+1])
        return output
