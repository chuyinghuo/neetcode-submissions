class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = len(nums)*[0]

        for i in range(len(nums)):
            prod = 1 
            for j in range(len(nums)):
                if i == j:
                    continue 
                prod *= nums[j]
            res[i] = prod 
        return res

            
        