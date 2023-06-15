"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
typically using all the original letters exactly once.

Sol:
"""


class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        # keyVal = {}
        # for i in strs:
        #     keyVal[i] = ''.join(sorted(i))
        # print(keyVal)
        # result = {}
        # for key, val in keyVal.items():
        #     result.setdefault(val, []).append(key)
        #
        # return list(result.values())

        keyVal = {}
        for i in strs:
            x = ''.join(sorted(i))
            if x in keyVal:
                keyVal[x].append(i)
            else:
                keyVal[x] = [i]

        return list(keyVal.values())

obj = Solution()
print(obj.groupAnagrams(["",""]))
print(obj.groupAnagrams(["abc","abc"]))