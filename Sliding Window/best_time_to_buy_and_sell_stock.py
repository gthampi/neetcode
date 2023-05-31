# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit = 0
        p1, p2 = 0, 1
        while p2 < len(prices):
            if prices[p1] < prices[p2]:
                max_profit = max(prices[p2] - prices[p1], max_profit)
            else:
                p1 = p2
            p2 += 1
        return max_profit
