class Solution:
    #just used the iterator as r pointer
    def lengthOfLongestSubstring(self, s):
        summ = 0 
        l = 0 
        for r in range(len(s)):
            if len(s[l:r+1]) == len(set(s[l:r+1])):
                summ = max(summ,r-l+1)
            else:
                l = l + 1
        return summ
