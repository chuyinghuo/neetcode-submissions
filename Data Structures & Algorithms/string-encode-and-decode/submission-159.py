class Solution:
    def encode(self, strs: List[str]) -> str:
        encoded_words = []

        for word in strs:
            #format length of word to be 4 letters
             word_length = f"{len(word):4}"
             encoded_words.append(word_length+word)
        return "".join(encoded_words)

       
    def decode(self, s: str) -> List[str]:
        decoded = []
        j = 0 
        
        while j < len(s):
            word_length = int(s[j: j+4])
            j += 4
            word = s[j: j+word_length]
            decoded.append(word)
            j += word_length
        return decoded
            


        