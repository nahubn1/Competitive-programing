from collections import Counter
class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        moves = 0
        stack = []
        for i in nums:
            if stack and i <= stack[-1]:
                moves += (stack[-1] - i + 1)
                stack.append(stack[-1] + 1)
            else:
                stack.append(i)
        return moves
