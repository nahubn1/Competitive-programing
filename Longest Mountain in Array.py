class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        s, m , e = 0, 1, 2
        maxLen = 0
        mountLen = 0
        while m <= len(arr) - 2:
            # print(s, m, e)
            if arr[s] < arr[m] and arr[m] > arr[e]:
                # print('here', m, arr[m])
                mountLen += 3
                while s >= 1 and arr[s] > arr[s-1]:
                    mountLen += 1
                    s -= 1
                while e <= len(arr) - 2 and arr[e] > arr[e+1]:
                    mountLen += 1
                    e += 1
                # print('mt len', mountLen)
                maxLen = max(maxLen, mountLen)
                mountLen = 0
                m = e+1
                e, s = m+1, m-1  
            else:
                s, m, e = s+1, m+1, e+1
                
        return maxLen
