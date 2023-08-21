"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters
and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters
include letters and numbers.
Given a string s, return true if it is a palindrome, or false otherwise.

Example 1:
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

Example 2:
Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.

Example 3:
Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.

Sol: Remove the non-alphanumeric characters from string and convert the string to lower case.
Take two pointers and move one pointer from beginning and the other from end to mid. each loop,
compare  values at both indexes. If they are not equal at any point return False, Else return False at the end.
"""


import re
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = re.sub(r'[\W_]', '', s).lower()
        j = len(s)-1
        for i in range(0,len(s)//2):
            if s[i] != s[j]:
                return False
            j -= 1
        return True

# Time Complexity: O(n)

obj = Solution()
print(obj.isPalindrome('ab_a'))
print(obj.isPalindrome('Ha@%n am#$asa'))
print(obj.isPalindrome('A man, a plan, a canal: Panama'))
print(obj.isPalindrome(''))