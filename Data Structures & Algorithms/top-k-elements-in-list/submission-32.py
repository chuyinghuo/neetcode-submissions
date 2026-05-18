from collections import defaultdict 
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        for n in nums:
            count[n] += 1 
        sortedCount = dict(sorted(count.items(), key=lambda n: n[-1], reverse = True))
        res = list(sortedCount.keys())
        return res[0: k]


        

        