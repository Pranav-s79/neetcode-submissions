class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        max_prof = 0
        min_price = float('inf')
        
        for price in prices:
            if price<min_price:
                min_price = price
            else:
                w = price - min_price

                max_prof = max(max_prof,w)

        return max_prof

