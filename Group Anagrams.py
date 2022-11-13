class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        all_anagrams = {}
        for string in strs:
            anagram  = ''.join(sorted(string))
            if anagram in all_anagrams:
                all_anagrams[anagram].append(string)
            else:
                all_anagrams[anagram] = [string]
        return all_anagrams.values()
