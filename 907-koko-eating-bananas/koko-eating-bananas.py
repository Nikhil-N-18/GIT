class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n = len(piles)
        total = sum(piles)
        low = (total + h - 1)//h
        high = (total - 2 * n+h+1)//(h-n+1)
        while low < high:
            mid = low + (high-low)//2
            time = 0
            for i in range(n):
                time += (piles[i] + mid - 1)//mid
            if time > h:
                low = mid + 1
            else:
                high = mid
        return low