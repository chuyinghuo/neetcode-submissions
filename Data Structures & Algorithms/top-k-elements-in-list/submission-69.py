from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        counts = Counter(nums)
        heap = []
     
        for value, freq in counts.items():
            if len(heap) < k:
                heapq.heappush(heap, (freq, value))
            elif freq > heap[0][0]:
                heapq.heapreplace(heap, (freq, value))
        return [value for freq, value in heap[ :k]]
        
            



        
        
        