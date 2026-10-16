class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low = max(weights)
        high = sum(weights)
        while low <= high:
            mid = (low + high)>>1
            if self.ispossible(weights,days,mid):
                high = mid-1
            else:
                low = mid + 1
        return low
    def ispossible(self,weights:List[int],days:int,cap:int)->bool:
        load = 0
        days1 = 1
        for i in weights:
            if load + i > cap:
                days1 += 1
                load = 0
            load += i
        return days1 <= days