class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        sortedNums = nums
        i = 0
        solutions = []

        while i <= len(sortedNums)-1:
            if i > 0 and sortedNums[i] == sortedNums[i-1]:
                i+=1
                continue
            l=i+1
            r=len(sortedNums)-1
            
            while l<r:
                if sortedNums[i] + sortedNums[l] + sortedNums[r] == 0:
                    solutions.append([sortedNums[i],sortedNums[l],sortedNums[r]])
                    r-=1
                    l+=1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1

                    # Skip duplicate third values
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
                elif sortedNums[i] + sortedNums[l] + sortedNums[r] > 0:
                    r-=1
                else:
                    l+=1

            i+=1


        return solutions
