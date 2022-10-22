class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:

        search  = {}
        for char in p:
            if char in search:
                search[char] += 1
            else:
                search[char] = 1
        
        start = -len(p) + 1
        anagrams = []
        not_found = len(p)
        
        for end in range(len(s)):
            if s[end] in search: 
                search[s[end]] -= 1
                if search[s[end]] >= 0:
                    not_found -= 1
            
            if not_found == 0:
                anagrams.append(start)
                
            if start >= 0 and s[start] in search:
                search[s[start]] += 1
                if search[s[start]]  > 0:
                    not_found += 1
            
            start += 1
                
        return anagrams 
