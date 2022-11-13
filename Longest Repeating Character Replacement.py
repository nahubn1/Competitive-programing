from collections import Counter
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count, start = Counter([]), 0
        maxLen = 0
        for end in range(len(s)):
            count[s[end]] += 1
            most_freq = max(count.values())
            while (end-start)+1 - most_freq > k:
                count[s[start]] -= 1
                most_freq = max(count.values())
                start += 1
            maxLen = max(maxLen, (end-start)+1)
        return maxLen
