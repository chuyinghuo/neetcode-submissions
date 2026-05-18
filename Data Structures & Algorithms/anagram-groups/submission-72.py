from collections import defaultdict 
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        orders = defaultdict(list)
        for word in strs:
            orders["".join(sorted(word))].append(word)
        return list(orders.values())