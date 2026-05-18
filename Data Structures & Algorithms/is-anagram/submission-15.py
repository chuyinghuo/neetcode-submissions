from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sd = defaultdict(int)
        td = defaultdict(int)

        for i in s:
            sd[i] += 1 
        
        for n in t:
            td[n] += 1
        return sd == td

