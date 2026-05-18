from collections import defaultdict 
from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        orders = defaultdict(list)
        for word in strs:
            freq = Counter(list(word))
            orders[frozenset(freq.items())].append(word)
        return list(orders.values())