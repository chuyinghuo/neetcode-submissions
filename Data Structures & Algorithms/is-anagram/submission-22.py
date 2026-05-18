from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        setS = Counter(s)
        setT = Counter(t)
        if setS == setT:
             return True
        else:
            return False
        
        