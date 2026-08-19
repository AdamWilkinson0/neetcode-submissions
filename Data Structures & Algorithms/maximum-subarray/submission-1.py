class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        rSum = nums[0]
        bSum = nums[0]
        
        for i in range(1, len(nums)):
            if rSum+nums[i] > bSum and rSum > 0:
                rSum += nums[i]
                bSum = rSum
            elif rSum < 0:
                rSum = nums[i]
                if rSum > bSum:
                    bSum = rSum
            else:
                rSum += nums[i]
        return bSum



        