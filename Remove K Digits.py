class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for c in num:
            while k and stack and c < stack[-1]:
                k -= 1
                stack.pop()
            stack.append(c)
        stack = ''.join(stack[:len(stack)-k])
        return str(int(stack)) if stack else "0"
