class Solution:
    def maxArea(self, heights: List[int]) -> int:

        left = 0 
        right = len(heights)-1
        global_max = 0 

        while left < right:
            area = min(heights[left], heights[right])*(right-left)
            global_max = max(area, global_max)

            if heights[left] <= heights[right]:
                left += 1 
            else:
                right -= 1 
        return global_max