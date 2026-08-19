class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1

        while l <= r:
            m = l+(r-l)//2
            if nums[m] > nums[len(nums)-1]:
                l = m+1
            elif l == m and r == m:
                return nums[m]
            elif nums[m] < nums[len(nums)-1]:
                r = m
        
