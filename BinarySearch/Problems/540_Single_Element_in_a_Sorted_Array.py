"""
You are given a sorted array consisting of only integers where every element appears exactly twice,
except for one element which appears exactly once.
Return the single element that appears only once.
Your solution must run in O(log n) time and O(1) space.
"""


class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start = 0
        end = len(nums) - 1
        while start < end:
            mid = start + ((end - start) // 2)  # In this condition definitely, the mid-value of the array
            # will be an even number for the first time as all the numbers are duplicated except for one.
            if mid % 2 == 0:  # Checking if the mid-value is multiple of two.
                if not nums[mid] ^ nums[mid - 1]:  # If mid-value, and the previous value are same,
                    end = mid - 2  # Then the left array can be considered as an array with required value as
                    # it has odd number of values and Hence, updating end-value to mid-2.
                elif not nums[mid] ^ nums[mid + 1]:  # If mid-value, and the next value are same,
                    start = mid + 2  # Then the right array can be considered as an array with required value as
                    # it has odd number of values and Hence, updating start-value to mid+2.
                else:  # If either of the conditions are not satisfied we can return mid-value as it is not duplicated
                    return nums[mid]  #
            else:  # Else if the mid-value is not multiple of two.
                if not nums[mid] ^ nums[mid - 1]:   # If mid-value, and the previous value are same,
                    start = mid + 1  # Then the right array can be considered as an array with required value as
                    # it has odd number of values and Hence, updating start-value to mid+1.
                elif not nums[mid] ^ nums[mid + 1]:  # If mid-value, and the next value are same,
                    end = mid - 1  # Then the left array can be considered as an array with required value as
                    # it has odd number of values and Hence, updating end-value to mid-1.
                else:  # If either of the conditions are not satisfied we can return mid-value as it is not duplicated
                    return nums[mid]

        return nums[start]
        # When the start and end pointers point at the same value and the value is at end/beginning of array,
        # and we try to compare it to the previous or next value it throws index out of range error
        # Hence, ending the loop when start = end and returning the start value.


obj1 = Solution()
assert obj1.singleNonDuplicate([1, 1, 2, 3, 3, 4, 4, 8, 8]) == 2  # Test Case 1
assert obj1.singleNonDuplicate([1, 1, 2, 2, 3, 3, 4, 4, 8]) == 8  # Test Case 2
assert obj1.singleNonDuplicate([1, 2, 2, 3, 3, 4, 4, 8, 8]) == 1  # Test Case 3
assert obj1.singleNonDuplicate([1, 1, 2, 2, 3, 3, 4, 8, 8]) == 4  # Test Case 4
assert obj1.singleNonDuplicate([8]) == 8  # Test Case 5
assert obj1.singleNonDuplicate([1, 1, 2]) == 2  # Test Case 6
