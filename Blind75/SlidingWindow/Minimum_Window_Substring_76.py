"""
Given two strings s and t of lengths m and n respectively, return the minimum window
substring of s such that every character in t (including duplicates) is included in the window.
If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.


Example 1:
Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.

Example 2:
Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.

Example 3:
Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.

Sol:
"""


class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        dic = dict([])
        for char in t:
            dic[char] = -1

        l = 0
        h = 0
        n = len(s)
        while h<n:
            if s[h] in dic:
                s[h] = h

        print(dic)


obj = Solution()
print(obj.minWindow("ADOBECODEBANC", "ABC"))
print(obj.minWindow("a", "a"))
print(obj.minWindow("a", "aa"))

