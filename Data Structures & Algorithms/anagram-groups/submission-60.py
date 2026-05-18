from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        #solution does not work because 
        for word in strs:
            wordset = Counter(word)
            if frozenset(wordset.items()) in anagrams.keys():
                anagrams[frozenset(wordset.items())].append(word)
            else:
                anagrams[frozenset(Counter(word).items())] = []
                if word not in anagrams[frozenset(Counter(word).items())]:
                    anagrams[frozenset(Counter(word).items())].append(word)
        return list(anagrams.values())




