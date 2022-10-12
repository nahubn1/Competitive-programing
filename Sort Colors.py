from copy import deepcopy
class Solution:
    def sortColors(self, nums: list[int]) -> None:
        numbs = deepcopy(nums)
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.clear()
        while len(numbs) > 0:
            mini = min(numbs)
            nums.append(mini)
            numbs.remove(mini)
