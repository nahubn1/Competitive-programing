from collections import Counter
from math import comb
class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        count, unique = Counter(arr), list(set(arr))
        unique.sort()
        occurance = 0
        for i in range(len(unique)):
            ptr1, ptr2, new_tar = i+1, len(unique)-1, target - unique[i]
            while ptr1 < ptr2:
                if unique[ptr1]+unique[ptr2] < new_tar:
                    ptr1 += 1
                elif unique[ptr1]+unique[ptr2] > new_tar:
                    ptr2 -= 1
                else:
                    occurance += (count[unique[i]] * count[unique[ptr1]] * count[unique[ptr2]]) 
                    ptr1 += 1
                    ptr2 -= 1
            if count[unique[i]] >= 2:
                new_target = target - 2*unique[i]
                if new_target != unique[i] and new_target in count:
                    occurance += (comb(count[unique[i]], 2) * count[new_target])
            if count[unique[i]] >= 3:
                if 3*unique[i] == target:
                    occurance += comb(count[unique[i]], 3)
                    
        return occurance % (10**9 + 7)
