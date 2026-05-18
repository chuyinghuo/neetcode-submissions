class Solution:

    def encode(self, strs: list[str]) -> str:
        res = ""
        for i, n in enumerate(strs):
            res += "¥" + str(len(n)) + "€" + n  
        print("the result is " + res)
        return res 

    def decode(self, s: str) -> list[str]:
        i = 0 
        res = []
        while i < len(s):
            if s[i] == "¥":
                i += 1 
                j = i 
                while s[j] != "€":
                    j += 1 
                length = int(s[i:j])
                i = j+1
                word = s[i: i+length]
                res.append(word)
                i += length 
            else:
                i += 1 
        return res 

    


        


        

