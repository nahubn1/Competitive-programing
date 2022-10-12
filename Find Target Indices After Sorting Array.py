class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        numbs = sorted(nums)
        result = []
        for i, numb in enumerate(numbs):
            if numb == target:
                result.append(i)
        return result


sol = Solution()
ans = sol.targetIndices([1,2,5,2,3], target = 2)
print(ans)
