"""
Given a string s, find the length of the longest
substring without repeating characters.

Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

Sol: Take two pointers low and high. Store each element into a set or a queue by moving high pointer
until an element is repeated. Keep updating the max value accordingly.
Once an element is repeated write a loop to remove all the elements
until s[low] is equal to the element repeated.Return the maxValue at the end
"""
from collections import deque
class Solution1(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        low = 0
        high = low + 1
        n = len(s)
        if n == 1 or n == 0:
            return n
        maxVal = 0
        charSet = set({s[low]})
        while high <= n-1:
            while s[high] in charSet:
                charSet.remove(s[low])
                low = low + 1

            charSet.add(s[high])
            high += 1
            maxVal = max(maxVal, len(charSet))

        return maxVal

# obj = Solution1()
# print(obj.lengthOfLongestSubstring("abcadcbb"))
# print(obj.lengthOfLongestSubstring("pwwkew"))
# print(obj.lengthOfLongestSubstring("bbbbb"))
# print(obj.lengthOfLongestSubstring("aa"))
# print(obj.lengthOfLongestSubstring("ac"))
# print(obj.lengthOfLongestSubstring(""))
# print(obj.lengthOfLongestSubstring(" "))
# print(obj.lengthOfLongestSubstring("bwf"))


#Using Queue

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        low = 0
        high = low + 1
        n = len(s)
        if n == 1 or n == 0:
            return n
        maxVal = 0
        queue = deque([s[low]])
        while high <= n-1:
            while s[high] in queue:
                queue.popleft()
                low = low + 1

            queue.append(s[high])
            high += 1
            maxVal = max(maxVal, len(queue))

        return maxVal


obj1 = Solution()
print(obj1.lengthOfLongestSubstring("abcadcbb"))
print(obj1.lengthOfLongestSubstring("pwwkew"))
print(obj1.lengthOfLongestSubstring("bbbbb"))
print(obj1.lengthOfLongestSubstring("aa"))
print(obj1.lengthOfLongestSubstring("ac"))
print(obj1.lengthOfLongestSubstring(""))
print(obj1.lengthOfLongestSubstring(" "))
print(obj1.lengthOfLongestSubstring("bwf"))