from collections import Counter
class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        count = Counter(arr)
        count = sorted(count.items(), key = lambda x:x[1], reverse = True)
        n = len(arr)
        tot = 0
        i = 0
        for num, quantity in count:
            i += 1
            tot += quantity
            if tot >= n/2:
                return i
