class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        tot = sum(arr[:k])
        res = 1 if tot/k >= threshold else 0
        for s in range(len(arr)-k):
            tot += (arr[s+k]-arr[s])
            if tot/k >= threshold:
                res += 1
        return res
