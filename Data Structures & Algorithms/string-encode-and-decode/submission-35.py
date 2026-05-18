class Solution:

    def encode(self, strs: List[str]) -> str:
        final = ""
        for word in strs:
            length = len(word)
            final += str(length) + "#" + word 
        return final

    def decode(self, s: str) -> List[str]:
        output = []
        i = 0
        while i < len(s):
            #start = s[(s.index("#")+1)]
          #  length = s[(s.index("#") - 1)]
            hash_pos = s.index("#", i)
            length = int(s[i: hash_pos])
            start = hash_pos + 1
            word = s[start: start+length]
            output.append(word)
            i = start + length
        return output 
        
