class WordDictionary:

    def __init__(self):
        self.dictionary = {}

    def addWord(self, word: str) -> None:
        d = self.dictionary

        for c in word:
            if c not in d:
                d[c] = {}
            d = d[c]
        d['#'] = '#'
        
    def search(self, word: str) -> bool:
        
        def dfs(d, i):
            if i == len(word):
                return '#' in d
            c = word[i]
            if c != '.':
                if c not in d:
                    return False 
                return dfs(d[c], i+1)
            #else c is equal to .

            for c in d:
                if c == '#':
                    continue     
                if dfs(d[c], i+1):
                    return True 
            return False

        return dfs(self.dictionary, 0)

        
