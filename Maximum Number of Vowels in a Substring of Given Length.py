class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = ['a', 'e', 'i', 'o', 'u']
        subLen = 0
        for i in range(k):
            if s[i] in vowels:
                subLen += 1
        maxLen = subLen
        for i in range(len(s)-k):
            if s[i] in vowels:
                subLen -= 1
            if s[i+k] in vowels:
                subLen += 1
            maxLen = max(maxLen, subLen)
            
        return maxLen
