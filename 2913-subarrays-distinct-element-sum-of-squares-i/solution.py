// 116 ms | 19.1 MB
class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        ans = []
        for i in range(len(nums)):
            for j in range(i+1, len(nums)+1):
                ans.append(len(set(nums[i:j]))**2)
        return sum(ans)