class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n < 4:
            return True if n == 1 else False
        else:
            return self.isPowerOfFour(n/4)
