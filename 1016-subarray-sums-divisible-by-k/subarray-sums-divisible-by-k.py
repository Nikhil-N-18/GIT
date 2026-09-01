class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        n = len(nums)
        map1 = {0:1}
        first = count = 0
        for i in range(n):
            first += nums[i]
            last = first % k
            if last in map1:
                count += map1[last]
                map1[last] +=1
                
            else:
                map1[last] = 1
        return count