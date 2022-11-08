class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        flight = [0]*n
        for s, e, seats, in bookings:
            flight[s-1] +=  seats
            if e<n: flight[e] -= seats 
        for i in range(1, n):
            flight[i] += flight[i-1]
        return flight
