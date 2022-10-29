import math
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        output = [0]*len(temperatures)
        stack = [(-1,math.inf)]
        for i, temp in enumerate(temperatures):
            while temp > stack[-1][1]:
                output[stack[-1][0]] =  i - stack[-1][0]
                stack.pop()
            else:
                stack.append((i, temp))
        
        return output
