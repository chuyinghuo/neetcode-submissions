class Solution:
    def canJump(self, nums: List[int]) -> bool:
        #time complexity: O(max(n)^n)
        #space complexity: O(n)
        n = len(nums)
        memo = {n-1: True}
        def canreach(i):
            if i in memo:
                return memo[i]

            for jump in range(1, nums[i]+1):
                if canreach(i+jump):
                    memo[i] = True 
                    return True
            memo[i] = False 
            return False
        return canreach(0)

