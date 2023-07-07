"""
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
The overall run time complexity should be O(log (m+n)).

Input - nums1 = [1,3], num2 = [2] Output - 2.00  # Testcase 1
Input - nums1 = [1,2], nums2 = [3,4] Output - 2.50  # Testcase 2


Crux of this is this.
What is the most favourable splitting point ?

Suppose array is X and Y

you want to split X into two parts let us call  X1 and X2 as the boundary elements in the halves  of X i.e

.......X1 | X2 ........
.......Y1 | Y2...........

Now when is the problem solved ? - you need to describe a condition when problem is solved

Suppose i say that X1 <= Y2 and Y1 <= X2 is the problem solved ?
Because now you will know the 4 elements who will be at the middle in the merged array.
Because that will be {X1 Y1 | X2 Y2}

then problem is just answered by [max(X1,Y1) + min(X2,Y2)]/2

Sol:
1) check the length of two arrays and make sure that A is smaller array and B is larger array
2) Assign both total length and half of the total length to variables. As median is the num at mid-point of total array.
3) Consider two points l & r for A array. Where L is left pointer initially pointing at 0
and r is right pointer initially pointing at len(A)-1
4) Write a loop to find median. We can loop it until median is return. so, while true:
5) i is calculated mid pointed of A array. j is half-i
6) We need to consider 4 pointers aLeft anf BLefts points at i,j respectively.
While, aRight and bRight points at next values of left pointers.
7) Whenever indexes reach out of bound, inf/-inf values are assigned accordingly for future comparisons of values.
8)  if aL<=bR and aR>=bL: we can return the median as either min value of (aR, bR) when there are odd num of values.
9) or we can return (max(aL, bL) + min(aR, bR)) / 2 when there are even no.of values.
10) else if: the above condition is not satisfied. if aL>bR we need to assign r as i-1
11) else: we need to assign l = i + 1 and continue the loop until median is returned.
"""


# Actual Solution in O(log(m+n))
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        A, B = nums1, nums2
        m = len(nums1)
        n = len(nums2)
        total = m + n
        half = total // 2

        if n < m:
            A, B = B, A

        l, r = 0, len(A) - 1
        while True:
            i = (l + r) // 2
            j = half - i - 2  # -2 because we have 2 zeros in A,B indexes

            aLeft = A[i] if i >=0 else float("-infinity")
            aRight = A[i + 1] if (i+1) < len(A) else float("infinity")
            bLeft = B[j] if j >=0 else float("-infinity")
            bRight = B[j + 1] if (j+1) < len(B) else float("infinity")

            if aLeft <= bRight and bLeft <= aRight:
                if total % 2:
                    return min(aRight, bRight)
                else:
                    return float((max(aLeft, bLeft) + min(aRight, bRight)) / 2)
            elif aLeft > bRight:
                r = i - 1
            else:
                l = i + 1


obj1 = Solution()
print(obj1.findMedianSortedArrays([4, 5, 6], [1, 2, 3]))
print(obj1.findMedianSortedArrays([1, 3], [2]))
print(obj1.findMedianSortedArrays([0,0], [0,0]))


# Brute force
class Solution1(object):
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
            return (arr[len3 // 2] + arr[(len3 // 2) - 1]) / 2


# obj1 = Solution1()
# print(obj1.findMedianSortedArrays([1, 3], [2]))
# print(obj1.findMedianSortedArrays([1, 2], [3, 4]))
