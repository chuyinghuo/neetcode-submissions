
from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        anagrams = defaultdict(list)

        for s in strs:
            s_set = frozenset(Counter(s).items())
            anagrams[s_set] = []
        
        for s in strs:
                count = frozenset(Counter(s).items())
                if count in anagrams:
                    anagrams[count].append(s)
        return list(anagrams.values())






        