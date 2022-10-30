from math import inf
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        minStack = [inf]
        maxStack = [-inf]
        s = 0
        min_i = 0
        max_i = 0
        longest = 0
        for e in range(len(nums)):
            
            while len(minStack) > min_i and nums[e] < minStack[-1]:
                minStack.pop()
            else:
                minStack.append(nums[e])
                
            while len(maxStack) > max_i and nums[e] > maxStack[-1]:
                maxStack.pop()
            else:
                maxStack.append(nums[e])
                
            while abs(maxStack[max_i] - minStack[min_i]) > limit:
                if maxStack[max_i] == nums[s]:
                    max_i += 1
                if minStack[min_i] == nums[s]:
                    min_i += 1
                s += 1
            
            longest = max(longest, e - s + 1)
                
        return longest
