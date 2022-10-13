class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        opers = ["+", "-", "*", "/"]
        stack = []
        
        for i in tokens:
            if i in opers:
                i_1 = stack[-1]
                stack.pop()
                i_2 = stack[-1]
                stack.pop()
                stack.append(str(int(eval(i_2+i+i_1))))
            else:
                stack.append(i)
        return int(stack[0])
