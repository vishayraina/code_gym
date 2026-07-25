class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mn = float("inf")
        res = 0
        for i in range(len(prices)):
            mn = min(mn, prices[i])
            res = max(prices[i]-mn, res)
        return res