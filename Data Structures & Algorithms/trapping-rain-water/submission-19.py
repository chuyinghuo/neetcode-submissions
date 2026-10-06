class Solution:
    def trap(self, height: List[int]) -> int:

        water = 0
        max_left = 0
        max_right = 0
        left = []
        right = []

        for i in range(len(height)):
            
            left.append(max_left)
            max_left = max(max_left, height[i])
        
        for val in reversed(height):
            right.append(max_right)
            max_right = max(max_right, val)
        right.reverse()
        
       # print(left)
      #  print(right)
        for i in range(len(height)):
            potential = min(left[i], right[i])
            water += max(0, potential-height[i])
        return water
        




