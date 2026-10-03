class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        ans = [0] * len(nums1)
        for i in range(len(nums1)):
            j=0
            while j<len(nums2) and nums2[j] != nums1[i] :
                j += 1
            j += 1
            while j < len(nums2) and nums2[j] <= nums1[i]:
                j += 1
            if j < len(nums2) :
                ans[i] = nums2[j]
            else:
                ans[i] = -1
        return ans