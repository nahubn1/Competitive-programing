class Solution:
    def partitionString(self, s: str) -> int:
        Set, res = set(s[0]), 1
        for i in range(1, len(s)):
            if s[i] in Set: 
                Set.clear()
                res += 1
            Set.add(s[i])
        return res
