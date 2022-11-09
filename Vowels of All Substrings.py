class Solution:
    @staticmethod
    def series(n):
        return int((n*(n+1))/2)
    def countVowels(self, word: str) -> int:
        vowels = set(['a', 'e', 'i', 'o', 'u'])
        sumVow = 0
        n = len(word)
        all_substrings = self.series(n)
        for i in range(n):
            if word[i] in vowels:
                sumVow += (all_substrings - (self.series(i) + self.series(n-1-i)))
        return sumVow
