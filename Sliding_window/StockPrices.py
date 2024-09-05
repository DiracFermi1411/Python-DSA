class Solution:
    def maxProfit(self, prices) -> int:
        prices_len = len(prices)
        if prices_len <= 1:
            return 0  # If there's only one price or no price, we can't make any profit
        
        max_profit = 0
        min_price = prices[0]
        
        for i in range(1, prices_len):
            # Calculate the profit if selling at the current price
            profit = prices[i] - min_price
            # Update the maximum profit if the current profit is greater
            if profit > max_profit:
                max_profit = profit
            # Update the minimum price seen so far
            if prices[i] < min_price:
                min_price = prices[i]
        
        return max_profit
                    



solution = Solution()
print