class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        profit = 0
        max_profit = 0
        if n<2:
            return 0
        else:
            buy = prices[0]
            for i in range(1,n):
                profit = prices[i] - buy
                if profit>max_profit:
                    max_profit = profit
                if prices[i] < buy:
                    buy = prices[i]
            return max_profit