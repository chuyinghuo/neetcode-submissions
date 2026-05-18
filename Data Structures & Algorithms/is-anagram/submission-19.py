class Solution:
    def isAnagram(self, s: str, t:str) -> bool:
        string1 = Counter(s)
        string2 = Counter(t)
        if len(set(s)) == len(set(t)) and string1 == string2:
            return True
        return False
