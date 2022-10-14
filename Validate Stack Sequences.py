class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        
        ptr = 0
        
        while len(popped) > 0:
            if popped[0] == pushed[ptr]:
                pushed.pop(ptr)
                popped.pop(0)
                ptr = ptr - 1 if ptr > 0 else 0
            else:
                if ptr < len(pushed)-1:
                    ptr += 1
                else:
                    return False
        return True
