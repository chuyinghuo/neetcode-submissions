class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}

        for word in strs:
            sortstrs = " ".join(sorted(word))
            if sortstrs in anagrams.keys():
                anagrams[sortstrs].append(word)
            else:
                anagrams[sortstrs] = []
                if word not in anagrams[sortstrs]:
                    anagrams[sortstrs].append(word)
        return list(anagrams.values())


