class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False 
        countS, countT = {}, {}
    
        for i in s:
            if i not in countS:
                countS[i] = 0
            countS[i] += 1

    
        for n in t:
            if n not in countT:
                countT[n] = 0
            countT[n] += 1
    
        return countS == countT