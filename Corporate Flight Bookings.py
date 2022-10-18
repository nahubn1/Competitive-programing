class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        res = [0]*(n+1)
        for start, end, seat in bookings:
            res[end] += seat
            res[start-1] += -seat
        
        for i in range(len(res)-2, -1, -1):
            
            res[i] += res[i+1]
        res.pop(0)
        return res
