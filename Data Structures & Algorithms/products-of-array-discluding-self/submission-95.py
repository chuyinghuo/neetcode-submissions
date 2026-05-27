#Brute force solution 
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        res = []
        for i in range(len(nums)):
            element = 1
            for j in range(len(nums)):
                if j != i:
                    element *= nums[j]
            res.append(element)
        return res

       

