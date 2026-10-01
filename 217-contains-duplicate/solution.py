// 23 ms | 32.3 MB
class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        arr = set()
        for num in nums:
            if num not in arr:
                arr.add(num)
            else:
                return True
        return False