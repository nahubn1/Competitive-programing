class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        changed.sort()
        hashmap = {}
        delete = {}
        for i in changed:
            delete[i] = 0
            if i in hashmap:
                hashmap[i] += 1
            else:
                hashmap[i]  = 1
                
        
        orginal = []
        n = len(changed)
        if n%2 == 1:
            return []
        i = 0
        # print(changed)
        while i < n-1:
            # print(i, changed[i])
            hashmap[changed[i]] -= 1
            if changed[i]*2 in hashmap and hashmap[changed[i]*2] > 0:
                hashmap[changed[i]*2] -= 1
                orginal.append(changed[i])
                delete[changed[i]*2] += 1
                # print(delete, changed[i])
                i += 1
                while i < n and delete[changed[i]] > 0:
                    # print('h1', delete, changed[i])
                    delete[changed[i]] -= 1
                    i += 1
                    
                    
            else:
                return []
            
        return orginal
