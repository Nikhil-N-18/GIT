class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        arr = [0]*(n+1)
        for booking in bookings:
            first = booking[0]
            middle = booking[1]
            last = booking[2]
            arr[first-1] += last
            arr[middle] -= last
        for i in range(1,n):
            arr[i] += arr[i-1]
        return arr[:n]