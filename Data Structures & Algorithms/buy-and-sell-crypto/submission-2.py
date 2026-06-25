class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0 
        for i, price in enumerate(prices):
            for j in range(i+1, len(prices)):
                curr = prices[j] - prices[i]
                res = max(curr, res)
        return res
