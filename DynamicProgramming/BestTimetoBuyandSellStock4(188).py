class Solution:
    def maxProfit(self, k, prices):
        n = len(prices)
        if n < 2 or k == 0:
            return 0
        
        
        if k >= n // 2:
            profit = 0
            for i in range(1, n):
                if prices[i] > prices[i - 1]:
                    profit += prices[i] - prices[i - 1]
            return profit
        
        # DP arrays
        buy = [-10**9] * (k + 1)
        sell = [0] * (k + 1)
        
        for price in prices:
            for i in range(1, k + 1):
                buy[i] = max(buy[i], sell[i - 1] - price)
                sell[i] = max(sell[i], buy[i] + price)
        
        return sell[k]