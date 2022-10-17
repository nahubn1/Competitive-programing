class Solution:
    def compress(self, chars: List[str]) -> int:
        
        s = []
        ptr1 = 0
        ptr2 = 0
        while ptr2 < len(chars):
            if ptr1 == ptr2:
                s.append(chars[ptr1])
                s.append(1)
                ptr2 += 1
            else:
                if chars[ptr1] == chars[ptr2]:
                    s[-1] += 1
                    ptr2 += 1
                else:
                    ptr1 += 1
        chars.clear()
        
        for i in s:
            if isinstance(i, int):
                if i != 1:
                    chars += list(str(i))
            else:
                chars.append(i)
