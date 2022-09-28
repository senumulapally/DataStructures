"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]]
such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.
"""


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        finalLis = []
        nums = sorted(nums)  # Sorting the array
        for i in range(0, len(nums)):
            tar = 0 - nums[i]  # Here, we are considering the first number as i and target sum as target - i
            finalLis = self.twoSum(nums[i + 1:len(nums)], tar, nums[i], finalLis) # Calculating remaining two numbers
            # in triplet. Sending the remaining list as nums to the twoList method.
        return finalLis

    def twoSum(self, nums, target, val, finalLis):
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
                x = [val, nums[i], nums[mid]]
                if nums[mid] == target - nums[i] and x not in finalLis:  # If the triplet is already present in the
                    # final list we are not adding it to the current list
                    finalLis.append(x)
                elif nums[mid] < target - nums[i]:
                    start = mid + 1
                else:
                    end = mid - 1
        return finalLis


obj1 = Solution()

assert obj1.threeSum([-1, 0, 1, 2, -1, -4]) == [[-1, -1, 2], [-1, 0, 1]] # Test Case 1
assert obj1.threeSum([0, 1, 1]) == []  # Test Case 2
assert obj1.threeSum([0, 0, 0]) == [[0, 0, 0]]  # Test Case 3
assert obj1.threeSum([0, 0, 0, 0]) == [[0, 0, 0]]   # Test Case 4
assert obj1.threeSum([-2, 0, 1, 1, 2]) == [[-2, 0, 2], [-2, 1, 1]]  # Test Case 5


# print(obj1.threeSum([-1, 0, 1, 2, -1, -4])) # Test Case 1
# print(obj1.threeSum([0, 1, 1]))  # Test Case 2
# print(obj1.threeSum([0, 0, 0]))  # Test Case 3
# print(obj1.threeSum([0, 0, 0, 0])) # Test Case 4
# print(obj1.threeSum([-2, 0, 1, 1, 2]))  # Test Case 5
