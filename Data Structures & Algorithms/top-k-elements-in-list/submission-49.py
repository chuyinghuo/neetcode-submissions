from collections import defaultdict 
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        freq = defaultdict(list)

        for num in nums:
            count[num] += 1 
        
        for num, cnt in count.items():
            freq[cnt].append(num)
        
        res = []
        for cnt in range(len(nums), 0, -1):
            for num in freq[cnt]:
                res.append(num)
            if len(res) == k:
                return res
        
       

        