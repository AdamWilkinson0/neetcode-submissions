class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        sortedArr = sorted(nums)
        finalSet = []

        for i in range(len(sortedArr)):
            l = i + 1
            r = len(sortedArr) - 1
            if i > 0 and sortedArr[i - 1] == sortedArr[i]:
                    continue

            while l < r:


                if sortedArr[r] + sortedArr[l] == -sortedArr[i]:
                    finalSet.append([sortedArr[i], sortedArr[l], sortedArr[r]])
                    l += 1
                    r-=1
                    while l < r and sortedArr[l] == sortedArr[l - 1]:
                        l += 1
                    
                elif sortedArr[r] + sortedArr[l] < -sortedArr[i]:
                    l += 1
                else:
                    r -= 1

        return finalSet
