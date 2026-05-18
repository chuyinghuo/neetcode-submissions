class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        counts = defaultdict(int)
        for n in nums:
            counts[n] += 1 
        for i in counts:
            if counts[i] > 1:
                return True  
        return False
