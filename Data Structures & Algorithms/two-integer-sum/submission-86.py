from collections import defaultdict 
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_indices = {}

        for index, num in enumerate(nums):
            nums_indices[num] = index 
        
        for index, num in enumerate(nums):
            if target-num in nums_indices and nums_indices[target-num] != index:
                return [index, nums_indices[target-num]]

