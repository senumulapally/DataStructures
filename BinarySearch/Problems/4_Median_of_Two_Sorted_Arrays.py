"""
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
The overall run time complexity should be O(log (m+n)).

Input - nums1 = [1,3], num2 = [2] Output - 2.00  # Testcase 1
Input - nums1 = [1,2], nums2 = [3,4] Output - 2.50  # Testcase 2
"""


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        i = 0
        j = 0
        len1 = len(nums1)
        len2 = len(nums2)
        arr = []
        while i < len1 and j < len2:
            if nums1[i] < nums2[j]:
                arr.append(nums1[i])
                i += 1
            elif nums1[i] > nums2[j]:
                arr.append(nums2[j])
                j += 1
            else:
                arr.append(nums1[i])
                arr.append(nums2[j])
                i += 1
                j += 1

        if j < len2:
            for p in range(j, len2):
                arr.append(nums2[p])
        if i < len1:
            for q in range(i, len1):
                arr.append(nums1[q])
        len3 = len(arr)
        if len3 % 2 > 0:
            return arr[len3 // 2]
        else:
            return (arr[len3 // 2] + arr[(len3//2) - 1]) / 2


obj1 = Solution()
print(obj1.findMedianSortedArrays([1, 3], [2]))
print(obj1.findMedianSortedArrays([1, 2], [3, 4]))
