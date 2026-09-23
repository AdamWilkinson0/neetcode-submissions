class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        appears = set()
        for i in range(len(nums)):
            if nums[i] in appears:
                return True
            appears.add(nums[i])

        return False
            