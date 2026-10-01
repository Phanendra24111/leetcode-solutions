// 3 ms | 22.7 MB
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        res = [0]*k
        freq = {}
        t = 0
        res = []
        for num in nums:
            freq[num] = freq.get(num,0) + 1
        s_freq = dict(sorted(freq.items(), key = lambda x: x[1],reverse = True))
        for key,values in s_freq.items():
            if t< k:
                res.append(key)
                t += 1
        return res