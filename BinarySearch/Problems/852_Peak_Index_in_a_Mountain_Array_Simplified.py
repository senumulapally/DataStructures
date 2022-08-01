class Solution(object):
    def peakIndexInMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        # When mid-value is less than it's next value, the low-pointer in updated to the next value of mid.
        # Else, High-pointer is updated to mid-1. the loop will stop when the low-pointer is reaches the
        # peak value and the high-pointer points to the previous index of peak value.
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


obj1 = Solution()
print(obj1.peakIndexInMountainArray([0, 1, 0]) == 1)
print(obj1.peakIndexInMountainArray([0, 2, 1, 0]) == 1)
print(obj1.peakIndexInMountainArray([0, 10, 5, 2]) == 1)
print(obj1.peakIndexInMountainArray([0, 2, 5, 10, 5, 2]) == 3)
print(obj1.peakIndexInMountainArray([0, 2, 5, 10, 11, 7, 6, 5, 2]) == 4)
