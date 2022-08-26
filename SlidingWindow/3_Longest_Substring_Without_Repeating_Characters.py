"""
Given a string s, find the length of the longest substring without repeating characters.
"""


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """


obj1 = Solution()
print(obj1.lengthOfLongestSubstring("abcabcbb"))
print(obj1.lengthOfLongestSubstring("bbbbb"))
print(obj1.lengthOfLongestSubstring("pwwkew"))
