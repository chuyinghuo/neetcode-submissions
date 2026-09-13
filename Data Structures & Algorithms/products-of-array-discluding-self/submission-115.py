class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #initalize length of array nums
        n = len(nums)
        result = [0] * n

        #two passes for O(n) without division symbol 

        left_product = 1
        for i in range(n):
            result[i] = left_product
            left_product *= nums[i]
        
        right_product = 1
        for i in range(n-1, -1, -1):
            result[i] *= right_product 
            right_product *= nums[i]
        return result
 

