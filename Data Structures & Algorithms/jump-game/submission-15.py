class Solution:
    def canJump(self, nums: List[int]) -> bool:
        #recursive 
        #time complexity: O(max(nums)^n)
        #space: O(n)
        #top down Dp approach
        #create memo hashmap
        #time complexity O(n^2)
        #space: O(n)

        n = len(nums)
        memo = {n-1: True}

        def can_reach(i):
            if i in memo:
                return memo[i] 
            
            for jump in range(1, nums[i]+1):
               if can_reach(i+jump):
                    memo[i] = True 
                    return True 
            memo[i] = False 
            return False 
        return can_reach(0)

            
