"""
You are given a string s and an integer k. You can choose any character of the string and change it to
any other uppercase English character. You can perform this operation at most k times.
Return the length of the longest substring containing the same letter you can get after performing the
above operations.

Example 1:
Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.

Example 2:
Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
There may exists other ways to achive this answer too.

Sol: Track the character frequencies using a dictionary
Increment the l value and decrease the count of s[l] as the window exceeds K
check the dic[s[h]] if it is less that K update the max value and increment h
"""


class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        dic = dict()
        n = len(s)
        l = 0
        h = 0
        maxvl = 0
        maxLen = 0
        while h < n:
            dic[s[h]] = 1 + dic.get(s[h], 0)
            maxvl = max(maxvl, dic[s[h]])
            if (h - l + 1) - maxvl > k:
                dic[s[l]] -= 1
                l += 1
            else:
                maxLen = max(maxLen, h - l + 1)
            h += 1
        return maxLen


obj = Solution()
print(obj.characterReplacement("ABAB", 2))
print(obj.characterReplacement("AABABBA", 1))
