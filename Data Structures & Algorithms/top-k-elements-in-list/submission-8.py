class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        dict = defaultdict(int)
        for n in nums:
            dict[n] += 1
        sorted_dict = sorted(dict.items(), key = lambda item: item[1], reverse = True)
        return [item[0] for item in sorted_dict[: k]]


        

        