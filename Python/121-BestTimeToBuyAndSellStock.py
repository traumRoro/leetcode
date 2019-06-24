# 121. Best Time to Buy and Sell Stock
# Say you have an array for which the ith element is the price of a given stock on day i.

# If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

# Note that you cannot sell a stock before you buy one.

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        min_price = prices[0]
        profit = 0
        for price in prices[1:]:
            if price - min_price > profit:
                profit = price - min_price
            elif price < min_price:
                min_price = price
        return profit