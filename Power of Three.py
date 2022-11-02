from math import log
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n < 3:
            return True if n == 1 else False
        else:
            return self.isPowerOfThree(n/3)
