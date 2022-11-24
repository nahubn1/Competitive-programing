class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals, stack = sorted(intervals, key=lambda x:x[0]), []
        for start, end in intervals:
            if stack and stack[-1][1] >= start:
                last_start, last_end = stack.pop()
                stack.append([last_start, max(last_end, end)])
            else:
                stack.append([start, end])
        return stack
