class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zeroCount = nums.count(0)

        if zeroCount > 1:
            return [0] * len(nums)

        if zeroCount == 1:
            total = 1
            for n in nums:
                if n != 0:
                    total = total*n
            return [total if n==0 else 0 for n in nums]
        total = 1
        for n in nums:
            total *= n
        return [total // n for n in nums]