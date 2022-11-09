class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        n = len(security)
        before = [0]*n #number of consecutive decreasing days before day i
        after = [0]*n #number of consecutive increasing days after day i
        for i in range(1, n):
            if security[i-1] >= security[i]:
                before[i] += before[i-1]+1
        for i in range(n-2, -1, -1):
            if security[i+1] >= security[i]:
                after[i] += after[i+1]+1
        goodDays = []
        for i in range(time, n-time):
            if before[i] >= time and after[i] >= time:
                goodDays.append(i)
        return goodDays
                
                
            
           
