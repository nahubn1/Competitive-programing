from math import floor, ceil
class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = ""
        for axis in range(2*len(s)-1):
            if axis%2 == 0:l, r, = int(axis/2), int(axis/2)
            else:l, r = floor(axis/2), ceil(axis/2)
                
            pal_str = ""
            while l>=0 and r<=len(s)-1:
                if s[l] == s[r]: pal_str = s[l:r+1]
                else: break
                l -=1
                r +=1
            if len(pal_str) > len(longest): longest = pal_str
            
        return longest
