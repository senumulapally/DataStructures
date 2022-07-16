class Solution:
    def searchRange(self, nums, target):
        startIndex, endIndex = -1, -1
        startIndex = self.findLeftMostIndex(nums, target)  # Calling leftRightMostIndex method to calculate
        # left most index
        if startIndex == len(nums)-1:  # Checking if the left most index is the last value of list
            endIndex = startIndex  # Assigning end index to last index
        else:
            endIndex = self.findLeftMostIndex(nums, target + 1) - 1  # else finding left most index of the
            # value next of the target value and subtracting 1 from the index obtained

        if startIndex <= endIndex:  # In some cases endIndex may be less than startIndex as we are searching for numbers
            # which aren't in the list while searching for endIndex
            return [startIndex, endIndex]
        return [-1, -1]  # If the above condition is not matched, it returns [-1,-1]

    def findLeftMostIndex(self, nums, target):
        start, end = 0, len(nums)-1  # Initiating start and end pointers
        while start < end:  # While loop is written for start<end because
            # we want to terminate the loop once the start-pointer is equal to end-pointer
            mid = start + (end - start) // 2  # Calculating Mid-pointer
            if nums[mid] < target:  # Checking if mid-pointer value is less than that of target
                start = mid + 1  # Updating start-pointer to the next index of mid-pointer
            else:
                end = mid  # If the Mid-pointer value is >= target value updating the end pointer to mid-pointer.
        return start  # Returning start pointer


object1 = Solution()
assert object1.searchRange([5, 7, 7, 8, 8, 10], 10) == [5, 5]  # Running Test Case 1
assert object1.searchRange([5, 7, 7, 8, 8, 10], 6) == [-1, -1]  # Running Test Case 2
assert object1.searchRange([], 0) == [-1, -1]  # Running Test Case 3
assert object1.searchRange([5, 7, 7, 8, 8, 10], 8) == [3, 4]  # Running Test Case 4
assert object1.searchRange([5, 7, 7, 8, 8, 10], 5) == [0, 0]  # Running Test Case 5
assert object1.searchRange([1, 1, 1], 1) == [0, 2]  # Running Test Case 6
