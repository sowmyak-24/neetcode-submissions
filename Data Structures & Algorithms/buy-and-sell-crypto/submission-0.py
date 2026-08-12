class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        l = len(prices)
        for i in range (l):
            for j in range (i+1, l):
                if prices[j] > prices[i]:
                    check = prices[j] - prices[i]
                    profit = max(check, profit)
        return profit