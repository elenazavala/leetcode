class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        buy, sell = 0, 1 
        
        while sell < len(prices):
            if prices[buy] < prices[sell]: # is it profitable?
                profit = prices[sell] - prices[buy]
                max_profit = max(profit,max_profit)
            else:
                buy = sell #we move our buy pointer wherever "sell" is, as it is lower and we want to buy at a lower price
            sell += 1 #and we advance the sell pointer
        
        return max_profit
