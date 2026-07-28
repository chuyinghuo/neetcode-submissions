class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        #Bruce force
        #create a set with all numbers from 0 to n 
        #for loop over the list and if n in the list is in the set than cont if not return false 
        
        return int(len(nums)*(len(nums)+1)/2 - sum(nums))