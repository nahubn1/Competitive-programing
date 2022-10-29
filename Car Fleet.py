class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(list(zip(position, speed)), key=lambda x:x[0], reverse  = True)
        stack = []
        for p, s in cars:
            if stack:
                p0, s0 = stack.pop()
                meetUpPos = (s0*p - s*p0)/(s0 - s) if s0!=s else -1
                if p <= meetUpPos <= target:
                    stack.append((p0, s0))
                else:
                    stack.append((p0, s0))
                    stack.append((p, s))
            else:
                stack.append((p, s))
                    
        return len(stack)
