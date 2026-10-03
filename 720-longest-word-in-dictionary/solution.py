// 7 ms | 19.5 MB
class Solution:
    def longestWord(self, words: List[str]) -> str:
        words.sort()
        words.sort(key = len, reverse= True)
        s = set(words)
        for word in words:
            if all(word[:i] in s for i in range(1, len(word))):
                return word
        return ''