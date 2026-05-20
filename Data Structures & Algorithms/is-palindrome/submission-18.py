class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_lower = s.lower()
        s_cleaned = ""
        for letter in s_lower:
            if letter != " " and letter.isalnum():
                s_cleaned += letter
        if len(s_cleaned) == 1:
            return True 
        i = 0  
        j = len(s_cleaned) - 1 
        while i < j:
            if s_cleaned[i] != s_cleaned[j]:
               return False 
            i += 1
            j -= 1 
        return True 