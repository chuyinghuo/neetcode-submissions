
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for word in strs:
            if ''.join(sorted(word)) not in groups:
                groups[''.join(sorted(word))] = []
            groups[''.join(sorted(word))].append(word)
        return groups.values()

        

        



        