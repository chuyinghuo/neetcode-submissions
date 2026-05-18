from collections import Counter 
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count = Counter(nums)
        for n in count:
            if count[n] > 1:
                return True 
        return False 
        
