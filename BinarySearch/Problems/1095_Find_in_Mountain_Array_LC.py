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
        while low <= high:
            mid = low + (high - low) // 2
            midVal = arr.get(mid)
            plusOne = arr.get(mid + 1)
            minusOne = arr.get(mid - 1)
            if midVal > plusOne and midVal > minusOne:
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
