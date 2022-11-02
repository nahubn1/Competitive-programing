class Solution:
    def calculate(self, s: str) -> int:
        oprs = {'/': 2, '*': 2, '+': 1, '-': 1, '.': 0}
        s += '.'
        stack = []
        for i in range(len(s)):
            if s[i] != ' ': 
                while s[i] in oprs and len(stack) >= 3 and oprs[stack[-2]] >= oprs[s[i]]:
                    num2 = stack.pop()
                    opr = stack.pop()
                    num1 = stack.pop()
                    stack.append(str(int(eval(num1+opr+num2))))
                if stack and stack[-1] not in oprs and s[i] not in oprs:
                    stack.append(stack.pop()+s[i])
                else:
                    stack.append(s[i])
                if s[i] == '.':
                    return stack[0]
