class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        n = max([trip[2] for trip in trips])
        graph = [0]*(n+1)
        
        for numPass, start, end in trips:
            graph[start] += numPass
            graph[end] -= numPass
        
        for i in range(len(graph)):
            if i != 0:
                graph[i] += graph[i-1]
            if graph[i] > capacity:
                return False
            
        return True
