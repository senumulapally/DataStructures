class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        new = list(range(0, len(nums)))
        indexDict = dict(zip(nums, new))  # Creating dictionary with list values and their indexes
        # so that we can still remember the index after sorting
        nums = sorted(nums)  # Sorting the array
        for i in range(0, len(nums)):
            start = i + 1  # Assigning start value as the index next to the current index
            # as the previous values are already looped, and we didn't find the target sum
            end = len(nums) - 1
            while start <= end:
                mid = start + (end - start) // 2
                if nums[mid] == target - nums[i]:
                    return [indexDict.get(nums[i]), indexDict.get(nums[mid])]  # Getting the index values of array
                    # before sorting using dictionary key-value pairs
                elif nums[mid] < target - nums[i]:
                    start = mid + 1
                else:
                    end = mid - 1
        return [-1, -1]  # If the required sum is not found returning [-1, -1]


obj1 = Solution()
assert obj1.twoSum([2, 7, 11, 15], 9) == [0, 1]  # Test Case 1
assert obj1.twoSum([0, 4, 3, 0], 0) == [0, 3]  # Test Case 2
assert obj1.twoSum([3, 2, 4], 6) == [1, 2]  # Test Case 3
