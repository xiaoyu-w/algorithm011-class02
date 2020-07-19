class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        买卖股票的最佳时机 II
        """
        total = 0
        for i in range(len(prices)-1):
            if prices[i+1] > prices[i]:
                total += prices[i+1] - prices[i]
        return total