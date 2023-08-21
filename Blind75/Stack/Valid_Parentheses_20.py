"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.


Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false

Sol: Create Dictionary with closing brackets are keys, and opening brackets are Values
Create an array, if char is pairs.values() add it to the stack
elif char is in pairs.keys, pop the stack and check if it equal to the char.. else return False
Once the whole loop is completed, we can return True is stack is empty, else False (i.e., return not stack)

"""


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        length = len(s)
        pairs = {')': '(', '}': '{', ']': '['}
        stack = []
        if length % 2:
            return False
        for char in s:
            if char in pairs.values():
                stack.append(char)
            elif char in pairs.keys():
                if not stack or stack.pop() != pairs[char]:
                    return False
        return not stack


obj = Solution()
# print(obj.isValid("(]"))
print(obj.isValid("({"))
