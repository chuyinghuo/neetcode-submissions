class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        return "01".join("".join(ch * 2 for ch in words) for words in strs) + "01"

    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        decoded = []
        current_word = ""
        i = 0 
        while i < len(s)-1:
            pair = s[i:i+2]
            if pair[0] == pair[1]:
                current_word += pair[0]
            else:
                decoded.append(current_word)
                current_word = ""
            i += 2
        return decoded