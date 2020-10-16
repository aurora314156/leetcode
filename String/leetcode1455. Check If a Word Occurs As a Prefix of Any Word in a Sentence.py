class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        ind = 1
        for w in sentence.split():
            if w.find(searchWord) == 0:
                return ind
            ind += 1
        return -1