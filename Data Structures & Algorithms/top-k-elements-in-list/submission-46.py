from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)

        sortedCounts = sorted(counts.items(), key = lambda item: -item[1])

        relevant = sortedCounts[: k]
        return [key for key, value in relevant]


       

        