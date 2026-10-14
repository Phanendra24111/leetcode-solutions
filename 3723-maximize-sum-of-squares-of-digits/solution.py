// 2 ms | 21.1 MB
class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        shortest = "9" * (sum//9) + str(sum % 9 or "")
        return shortest.ljust(num,"0") if len(shortest) <= num else ""