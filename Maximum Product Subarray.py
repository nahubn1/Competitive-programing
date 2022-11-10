from math import inf
from numpy import prod
class Solution:
    @staticmethod
    def count_neg(ls):
        ans =  0
        for i in ls:
            if i < 0: ans += 1
        return ans
    def maxProduct(self, nums: List[int]) -> int:
        new = [[]]
        for num in nums:
            if num == 0:
                new.append([0])
                new.append([])
            else:
                new[-1].append(num)
        split = []
        for ls in new:
            if ls != []:split.append(ls)
        maxProd = -inf
        for ls in split:
            lsProd = 1
            n_neg = self.count_neg(ls)
            if n_neg%2 == 0:
                lsProd = prod(ls)
                maxProd = max(maxProd, lsProd)
            else:
                for num in ls:
                    if num < 0: n_neg -= 1
                    lsProd *= num
                    maxProd = max(maxProd, lsProd)
                    if n_neg == 0: lsProd = 1
                n_neg, lsProd = self.count_neg(ls), 1
                for num in reversed(ls):
                    if num < 0: n_neg -= 1
                    lsProd *= num
                    maxProd = max(maxProd, lsProd)
                    if n_neg == 0: lsProd = 1
            
        return int(maxProd)
