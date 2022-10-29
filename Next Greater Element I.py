class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        output = {num: -1 for num in nums1}
        for num in nums2:
            while stack and num > stack[-1]:
                last_num = stack.pop()
                if last_num in output:
                    output[last_num] = num
            
            stack.append(num)
            
        return output.values()
