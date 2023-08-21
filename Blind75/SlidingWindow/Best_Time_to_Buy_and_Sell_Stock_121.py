"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing
a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Example 1:
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

Example 2:
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.

Sol:
If High val<Low val, keep incrementing low+1, high+1.
else, calculate max val and increment high val.
Doing so, low pointer stops at lowest value until high value is < low value.
"""


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) <= 1:
            return 0
        low = 0
        high = low + 1
        n = len(prices)
        maxPrice = 0
        while high < n and low < n:
            if prices[high]<prices[low]:
                low += 1
                high += 1
            else:
                maxPrice = max(maxPrice, prices[high] - prices[low])
                high += 1
        return maxPrice

obj = Solution()
print(obj.maxProfit([7,1,5,3,6,4]))