class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        outPut = [0]*len(temperatures)
        stack = [(0, temperatures[0])]
        for day, temp in enumerate(temperatures):
            if day:
                while stack and temp > stack[-1][1]:
                    last_day, last_temp = stack.pop()
                    outPut[last_day] = day-last_day
                else:
                    stack.append((day, temp))
        return outPut
