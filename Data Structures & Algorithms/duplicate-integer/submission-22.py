from collections import Counter
class Solution:
# 2. Can we assume this is a 1D array?
# Will we be given any empty arrays?
    def hasDuplicate(self, nums: List[int]) -> bool:
        c = Counter(nums)

        for (key, value) in c.items():
            if value >= 2:
                return True 
        return False
        