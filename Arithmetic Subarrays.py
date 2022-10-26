class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        boolList = []
        for i in range(len(l)):
            seq = sorted(nums[l[i]:r[i]+1])
            diff = [seq[i] - seq[i+1] for i in range(len(seq)-1)]
            i = 1
            while i < len(diff):
                if diff[i] != diff[i-1]:
                    boolList.append(False)
                    break
                i += 1
            else:
                boolList.append(True)
                
        return boolList
