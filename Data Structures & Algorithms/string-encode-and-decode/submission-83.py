class Solution:

    def encode(self, strs: list[str]) -> str:
        res = ""
        for i, n in enumerate(strs):
            res += "¥" + str(len(n)) + "€" + n  
        print("the result is " + res)
        return res 

    def decode(self, s: str) -> list[str]:
        res = []
        for i, n in enumerate(s):
            if n == "¥":
                start = s.find("€", i)+1
                print("start is " + str(start))
                index2 = s.find("€", start-2)
                print("the index is " + str(index2)) 
                end = int(s[i+1: index2])
                print("end is " + str(end))
                word = s[start: start+end]
                res.append(word)
        return res 

    


        

