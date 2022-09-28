"""
Given an integer array nums, return 3 indexes where sum of integers at that indexes = target.
"""


class Solution(object):
    def threeSum(self, nums, target):
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
            tar = target - nums[i]  # Here, we are considering the first number as i and target sum as target - i
            test = self.twoSum(nums[i + 1:len(nums)], tar) # In this method we'll be considering the rest of the List
            # as input list and we'll find twoSum
            if test != [-1, -1]:
                test.append(nums[i])
                return sorted([indexDict.get(test[0]), indexDict.get(test[1]), indexDict.get(test[2])])
        return [-1, -1, -1]

    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(0, len(nums)):
            start = i + 1  # Assigning start value as the index next to the current index
            # as the previous values are already looped, and we didn't find the target sum
            end = len(nums) - 1
            while start <= end:
                mid = start + (end - start) // 2
                if nums[mid] == target - nums[i]:
                    return [nums[i], nums[mid]]
                elif nums[mid] < target - nums[i]:
                    start = mid + 1
                else:
                    end = mid - 1
        return [-1, -1]  # If the required sum is not found returning [-1, -1]


obj1 = Solution()
assert obj1.threeSum([1, 2, 7, 6, 11, 15], 9) == [0, 1, 3]  # Test Case 1
assert obj1.threeSum([1, 2, 7, 6, 11, 15], 27) == [0, 4, 5]  # Test Case 2
assert obj1.threeSum([1, 2, 7, 11, 15], 19) == [0, 2, 3]  # Test Case 3
