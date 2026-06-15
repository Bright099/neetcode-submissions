class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        max_profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[left]:
                profit = prices[i] - prices[left]
                if profit > max_profit:
                    max_profit = profit
            else:
                left = i
        return max_profit
        