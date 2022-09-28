"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]]
such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.
"""


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        output = set()

        nums.sort()

        # Outer for loop for i.
        for i in range(0, len(nums) - 2):

            # Outer for loop for j.
            for j in range(i + 1, len(nums) - 1):

                elem = 0 - (nums[i] + nums[j])

                low = j + 1
                high = len(nums) - 1

                # Binary search on the rest of the array to find the compliement.
                while low <= high:
                    mid = low + (high - low) // 2

                    # Divide the array into two halves. The first half is about the list of elements that is
                    # less than compliment.
                    if nums[mid] < elem:
                        low = mid + 1
                    else:
                        high = mid - 1

                # When the binary search is done, the low can point to the end of the array. In this case the compliment is not present.
                if low == len(nums):
                    continue

                # If we are here, there is atleast one element, that is greater than or equal to compliment.
                # Run sequential search on the reminder. In worst case this is 0👎
                while low <= len(nums) - 1:
                    if nums[low] != elem:
                        break

                    output.add(tuple([nums[i], nums[j], nums[low]]))
                    low = low + 1

        return output