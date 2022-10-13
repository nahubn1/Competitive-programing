class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = ''
        open_brakets = []
        for i, x in enumerate(s):
            stack += x
            # print(f'i = {i}', f'x = {x}', f'stack ={stack}')
            if x == '(':
                open_brakets.append(len(stack)-1)
            elif x == ')':
                before = stack[open_brakets[-1]:i+1]
                after = ''.join(reversed(list(before)))[1:-1]
                open_brakets.pop()
                # print(f'before = {before}', f'after = {after}')
                
                stack = stack.replace(before, after)
                
        return stack
