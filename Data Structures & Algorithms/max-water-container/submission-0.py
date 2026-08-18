class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights)-1
        mArea = 0
        
        while l < r:
            width = r-l
            if heights[l] < heights[r]:
                height = heights[l]
                l += 1
            else:
                height = heights[r]
                r -= 1
            area = width * height

            if area > mArea:
                mArea = area
            
        
        return mArea
