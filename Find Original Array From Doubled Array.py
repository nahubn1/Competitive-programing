from collections import Counter
class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        changed.sort()
        count = Counter(changed)
        
        if len(changed)%2 == 1:
            return []
        
        orginal = []
        for num in changed:
            if count[num]:
                count[num] -= 1
                if count[num*2]:
                    orginal.append(num)
                    count[num*2] -= 1
                else:
                    return []
        
        return orginal  
