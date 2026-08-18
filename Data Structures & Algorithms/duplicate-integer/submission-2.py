class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        occurred = set()
        for i in range(len(nums)):
            if nums[i] in occurred:
                return True
            else:
                occurred.add(nums[i])
        return False