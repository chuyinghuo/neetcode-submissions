class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_water = 0
        for iw, ih in enumerate(heights):
            for jw, jh in enumerate(heights):
                height = min(ih, jh)
                width = abs(iw-jw)
                water = height*width 
                max_water = max(max_water, water)
        return max_water
