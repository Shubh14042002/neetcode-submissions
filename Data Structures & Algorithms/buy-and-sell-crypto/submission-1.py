class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cheapest_so_far = None
        profit = 0
        best_profit = 0 
        for price in prices:
            if cheapest_so_far == None:
                cheapest_so_far = price
            elif price < cheapest_so_far:
                cheapest_so_far = price
            elif price > cheapest_so_far:
                profit = price - cheapest_so_far
                if profit > best_profit:
                    best_profit = profit
        
        return best_profit
