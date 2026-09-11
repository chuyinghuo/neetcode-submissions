class Solution:

    def encode(self, strs: List[str]) -> str:

        coded = []

        for word in strs:
            word_len = f"{len(word):4}"
            coded.append(word_len+word)
        return "".join(coded)

    def decode(self, s: str) -> List[str]:
        res = []
        j = 0
        while j < len(s):
            word_length = int(s[j:j+4])
            j += 4
            word = s[j:j+word_length]
            res.append(word)
            j += word_length
        return res

