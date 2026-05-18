class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = len(nums)*[0]

        for i, x in enumerate(nums):
            prod = 1 
            for j, n in enumerate(nums):
                if i == j:
                    continue 
                prod *= nums[j] 
            res[i]= prod
        return res


            
        