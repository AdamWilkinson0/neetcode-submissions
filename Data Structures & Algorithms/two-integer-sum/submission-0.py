class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = {}
        for i in range(len(nums)):
            n = nums[i]
            remainder = target - n
            if remainder in hm:
                return [hm[remainder], i]
            else:
                hm[n] = i
            