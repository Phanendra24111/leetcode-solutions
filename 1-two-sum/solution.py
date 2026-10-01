// 4 ms | 20.5 MB
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        numdict = {}
        n = len(nums)
        for i in range(n):
            numdict[nums[i]] = i
        for i in range(n):
            com = target - nums[i]
            if com in numdict and numdict[com] != i:
                return [i, numdict[com]]
        return []