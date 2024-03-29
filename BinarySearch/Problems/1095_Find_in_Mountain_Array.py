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
        if mountain_arr[peak] == target:
            return peak
        else:
            index = self.search(target, mountain_arr[0:peak], False)
            if index == -1:
                index = self.search(target, mountain_arr[peak: len(mountain_arr)], True)
                if index != -1:
                    return peak + index
        return index

    def findPeak(self, arr):
        low = 0
        high = len(arr) - 1
        while low <= high:
            mid = low + (high - low) // 2
            if arr[mid] > arr[mid + 1] and arr[mid] > arr[mid - 1]:
                return mid
            elif arr[mid] < arr[mid + 1]:
                low = mid + 1
            else:
                high = mid - 1

    def search(self, target, arr, isRight):
        low = 0
        high = len(arr) - 1
        while low <= high:
            mid = low + (high - low) // 2
            if (arr[mid] > target and isRight) or (arr[mid] < target and not isRight):
                low = mid + 1
            else:
                high = mid - 1

        if low == len(arr) or arr[low] != target:
            return -1
        return low


obj1 = Solution()
# print(obj1.findInMountainArray(3, [1, 2, 4, 5, 3, 1]) == 4)
# print(obj1.findInMountainArray(3, [1, 2, 3, 4, 5, 3, 1]) == 2)
# print(obj1.findInMountainArray(5, [1, 2, 3, 4, 5, 3, 1]) == 4)
# print(obj1.findInMountainArray(6, [1, 2, 3, 4, 5, 3, 1]) == -1)
# print(obj1.findInMountainArray(3, [0, 1, 2, 4, 2, 1]) == -1)
# print(obj1.findInMountainArray(0, [0, 1, 0]) == 0)
# print(obj1.findInMountainArray(1, [0, 1, 0]) == 1)
# print(obj1.findInMountainArray(2, [0, 5, 2]) == 2)
print(obj1.findInMountainArray(0, [3, 5, 3, 2, 0]))
