class Solution:
    
    @staticmethod
    def direction(parentheses):
        if parentheses in ['(', '[', '{']:
            return 'O'
        else:
            return 'C'
        
    @staticmethod
    def match(parentheses):
        if parentheses == '(':
            return ')'
        elif parentheses == '[':
            return ']'
        elif parentheses == '{':
            return '}'
    
    def isValid(self, s: str) -> bool:
        br = list(s)
        depth = 0
        i = 0
        while len(br) > 0:
            # print('br = ',''.join(br))
            # print('i = ', i, ', depth = ', depth)
            if self.direction(br[i]) == 'O':
                try:
                    next_ = br[i+1]
                except IndexError:
                    return False
                
                if self.direction(br[i+1]) == 'O':
                    i+=1
                    depth += 1
                else:
                    if br[i+1] == self.match(br[i]):
                        br.pop(i)
                        br.pop(i)
                        if depth > 0:
                            i -=1
                            depth -=1
                    else:
                        return False
            else:
                return False
        
        return True
