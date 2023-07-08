"""
You are given an integer array height of length n. There are n vertical lines drawn such that
the two endpoints of the ith line are (i, 0) and (i, height[i]).
Find two lines that together with the x-axis form a container, such that the container contains the most water.
Return the maximum amount of water a container can store.
Notice that you may not slant the container.

Example 1:
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7].
In this case, the max area of water (blue section) the container can contain is 49.

Example 2:
Input: height = [1,1]
Output: 1

Sol: Consider two pointers, Low and high pointing at first and last indexes.
Calculate the area each time we enter the loop
if high pointer height ie larger than low pointer, move low pointer, vice-versa.
Area calculation: consider min of two heights at low,high pointers and multiply it with diff of high-low indexes

extra condition: The value when diff of high,low is multiplied with max value in height array is
less than the current maxArea value, we can break the loop and return the maxArea.
Because, even if we continue with the loop we will never get the val greater than current maxArea.
"""


class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        low = 0
        high = len(height) - 1
        maxArea = 0
        h = max(height)
        while low < high:
            maxArea = max(maxArea, (min(height[low], height[high]) * (high - low)))
            if height[high] > height[low]:
                low += 1
            else:
                high -= 1
            if (high - low) * h < maxArea:
                break
        return maxArea

obj = Solution()
print(obj.maxArea([1,8,6,2,5,4,8,3,7]))