class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pairs = {}

        for i in range(len(nums)):
            if target-nums[i] in pairs:
                return [pairs.get(target-nums[i]), i]

            pairs[nums[i]] = i
        
            