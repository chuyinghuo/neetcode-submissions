
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        num_dict = {}
        
        for index, num in enumerate(nums):
           # num_dict[num] = index
            left = target - num 
            if left in num_dict and num_dict[left] != index:
                return [num_dict[left], index]
            num_dict[num] = index
        return []
    