# @leet start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest_price = prices[0]
        best_price = max(prices[0:])
        diff_curr = best_price - prices[0]
        diff_max = diff_curr

        for i_price in range(1, len(prices)):
            if lowest_price < prices[i_price]:
                pass
            if prices[i_price] < lowest_price:
                lowest_price = prices[i_price]
                price_curr = prices[i_price]
                best_price = max(prices[i_price:])
                diff_curr = best_price - price_curr
                if diff_curr > diff_max:
                    diff_max = diff_curr
        return diff_max


# @leet end
