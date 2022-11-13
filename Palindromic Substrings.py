class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        for axis in range(2*len(s)-1):
            if axis%2 == 0:l, r, = int(axis/2), int(axis/2)
            else:l, r = floor(axis/2), ceil(axis/2)
                
            while l>=0 and r<=len(s)-1:
                if s[l] == s[r]: count+=1
                else: break
                l -=1
                r +=1
            
        return count
