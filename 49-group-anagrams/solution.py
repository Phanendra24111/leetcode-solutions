// 7 ms | 21.9 MB
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        freq = {}
        for s in strs:
            temp = "".join(sorted(s))
            if temp not in freq:
                freq[temp] = []
            freq[temp].append(s)
        res = []
        for key, values in freq.items():
            res.append(freq[key])
        return res