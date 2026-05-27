#Brute force solution 
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        numZeros = 0 
        prod = 1 
        res = []

        for i in range(len(nums)):
            if nums[i] == 0:
                numZeros += 1 
            else:
                prod *= nums[i]
        if numZeros > 1:
            return len(nums) * [0]
        if numZeros == 1:
            for i in range(len(nums)):
                if nums[i] == 0:
                    res.append(prod)
                else:
                    res.append(0)
        if numZeros == 0:
             for i in range(len(nums)):
                res.append(prod//nums[i])
        return res
       

