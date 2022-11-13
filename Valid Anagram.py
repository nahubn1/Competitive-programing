from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sCount, tCount = Counter(list(s)), Counter(list(t)) 
        for char in sCount.keys():
            if sCount[char] == tCount[char]: tCount[char] = 0
            else:return False
        return True if sum(tCount.values()) == 0 else False
