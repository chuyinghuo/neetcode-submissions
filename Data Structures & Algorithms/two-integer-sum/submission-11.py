class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
       for i, n in enumerate(nums):
            for j, x in enumerate(nums):
                if i!=j and n+x == target:
                    if i<j:
                        return [i,j]
                    else:
                        return [j,i]
        