
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = Counter(nums)

        heap = []

        for key, val in d.items():
            if len(heap) < k or  val > heap[0][0]:
                heapq.heappush(heap, [val, key])
            if len(heap) > k:
                heapq.heappop(heap)
        return [i[1]for i in heap]



