class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        start = 0  # Initializing start-pointer
        end = len(nums) - 1  # Initializing end-pointer
        while start <= end:  # While loop ends when start-pointer is greater than end-pointer
            mid = start + ((end - start) // 2)  # Calculating mid-point (Integer Overflow exception handling)
            if target < nums[mid]:
                end = mid - 1  # Updating end-pointer when target is less than the mid-pointer value
            elif target > nums[mid]:
                start = mid + 1  # Updating start-pointer when target is greater than the mid-pointer value
            else:
                return mid  # Returning index when the target value matched mid-pointer value

        return -1  # Returning -1 when target value is not found in the given array.


search1 = Solution()  # Creating object
print(search1.search([-1, 0, 3, 5, 9, 12], 9))  # Running Test Case 1
print(search1.search([-1, 0, 3, 5, 9, 12], 2))  # Running Test Case 2
