class Solution:
    @staticmethod
    def collect(s, open_i):
        opens = 1
        res = ''
        for i in range(open_i+1, len(s)):
            if s[i] == '[':
                opens += 1
            elif s[i] == ']':
                opens -= 1
            
            if opens:
                res += s[i]
            else:
                return res
        return res
            
    def decodeString(self, s: str) -> str:
        i = 0
        count = ''
        decode = []
        value = 0
        while i < len(s):
            if s[i].isdigit():
                count += s[i]
                i += 1
            elif s[i].isalpha():
                string = s[i]
                i += 1
                decode.append((1, string))
            elif s[i] == '[':
                string = self.collect(s, i)
                i += (len(string) + 2)
                decode.append((int(count), string))
                count = ''
        
        output = []
        for c, strg in decode:
            if strg.isalpha():
                output.append(c*strg)
            else:
                output.append(c*self.decodeString(strg))
        
        return ''.join(output)
