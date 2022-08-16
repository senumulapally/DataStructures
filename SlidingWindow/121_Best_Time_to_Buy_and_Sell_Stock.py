"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future
to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
"""


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        diff = 0
        low = 0
        high = low + 1
        if len(prices) <= 1:  # Returning zero if the size is less than 1
            return 0

        while low < len(prices) and high < len(prices):
            if prices[high] < prices[low]:  # When price of high-pointer is less than low-pointer,
                # moving low-pointer to the next value and continuing the loop
                low += 1
                high = low + 1
            else:
                diff = max(diff, prices[high] - prices[low])  # Calculating the difference between high and low pointer
                # values and assigning max value to diff
                high += 1  # Moving the high-pointer to next value

        return diff


obj1 = Solution()
print(obj1.maxProfit([7, 1, 5, 3, 6, 4]) == 5)
print(obj1.maxProfit([7, 6, 4, 3, 1]) == 0)
print(obj1.maxProfit([7, 1, 5, 3, 6, 4, 2, 8, 9, 10]) == 9)
print(obj1.maxProfit([1, 2]) == 1)
print(obj1.maxProfit([2]) == 0)
