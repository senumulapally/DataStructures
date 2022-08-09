"""
(This problem is an interactive problem.)
You may recall that an array arr is a mountain array if and only if:
arr.length >= 3
There exists some i with 0 < i < arr.length - 1 such that:
arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
Given a mountain array mountainArr, return the minimum index such that mountainArr.get(index) == target.
If such an index does not exist, return -1.
You cannot access the mountain array directly. You may only access the array using a MountainArray interface:
MountainArray.get(k) returns the element of the array at index k (0-indexed).
MountainArray.length() returns the length of the array.
Submissions making more than 100 calls to MountainArray.get will be judged Wrong Answer.
Also, any solutions that attempt to circumvent the judge will result in disqualification.
"""
# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
# class MountainArray(object):
#    def get(self, index):
#        """
#        :type index: int
#        :rtype int
#        """
#
#    def length(self):
#        """
#        :rtype int
#        """

class Solution(object):
    def findInMountainArray(self, target, mountain_arr):
        """
        :type target: integer
        :type mountain_arr: MountainArray
        :rtype: integer
        """
        peak = self.findPeak(mountain_arr)
        if mountain_arr.get(peak) == target:
            return peak
        else:
            index = self.search(target, 0, peak, mountain_arr, False)
            if index == -1:
                index = self.search(target, peak + 1, mountain_arr.length(), mountain_arr, True)
        return index

    def findPeak(self, arr):
        low = 0
        high = arr.length() - 1
        arrLen = arr.length()
        while low <= high:
            mid = low + (high - low) // 2
            midVal = arr.get(mid)
            if (mid < arrLen - 1):
                plusOne = arr.get(mid + 1)
            if mid > 0:
                minusOne = arr.get(mid - 1)
            if (mid > 0 and midVal > plusOne) and (midVal > minusOne and mid < arrLen - 1):
                return mid
            elif midVal < plusOne:
                low = mid + 1
            else:
                high = mid - 1

    def search(self, target, min, max, arr, isRight):
        low = min
        high = max - 1
        while low <= high:
            mid = low + (high - low) // 2
            midVal = arr.get(mid)
            if (midVal > target and isRight) or (midVal < target and not isRight):
                low = mid + 1
            else:
                high = mid - 1

        if low == arr.length() or arr.get(low) != target:
            return -1
        return low


obj1 = Solution()
print(obj1.findInMountainArray(3, [1, 2, 4, 5, 3, 1]) == 4)
print(obj1.findInMountainArray(3, [1, 2, 3, 4, 5, 3, 1]) == 2)
print(obj1.findInMountainArray(5, [1, 2, 3, 4, 5, 3, 1]) == 4)
print(obj1.findInMountainArray(6, [1, 2, 3, 4, 5, 3, 1]) == -1)
print(obj1.findInMountainArray(3, [0, 1, 2, 4, 2, 1]) == -1)
print(obj1.findInMountainArray(0, [0, 1, 0]) == 0)
print(obj1.findInMountainArray(1, [0, 1, 0]) == 1)
print(obj1.findInMountainArray(1, [0, 1, 0]) == 1)
