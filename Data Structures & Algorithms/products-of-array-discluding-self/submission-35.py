class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total = 1
        for n in nums:
            if n != 0:
                total = total * n
        res = []  

        if 0 not in nums:
            for i in nums:
                current = total//i
                res.append(current)
            return res 

        if 0 in nums and not all(x == 0 for x in nums ):
            for i in nums:
                if i == 0 and nums.count(0) == 1:
                    if i == 0:
                        res.append(total)
                else:
                    res.append(0)
            return res 
        
        if all(x == 0 for x in nums):
            for i in nums:
                res.append(0)
        return res