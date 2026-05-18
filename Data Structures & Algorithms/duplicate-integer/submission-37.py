class Solution:
# 2. Can we assume this is a 1D array?
# Will we be given any empty arrays?
    def hasDuplicate(self, nums) -> bool:
        if len(nums) <= 1:
            return False 
        
        for i in range(0, len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j]:
                    return True 
        return False