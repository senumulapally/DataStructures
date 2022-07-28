"""
Given an integer array nums which is sorted in ascending order and all of its elements are unique and given also an
integer k, return the kth missing number starting from the leftmost number of the array.
"""


class Solution(object):
    def missingElement(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        def MissingElementsCount(val1, val2):
            return abs(val2 - val1)

        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = low + (high - low) // 2
            count = MissingElementsCount(nums[0] + mid, nums[mid])  # Calc number of values missing before mid-value
            if mid == len(nums) - 1:  # If the sequence has only one value
                # or if the mid-pointer has reached the final value in the array,
                # there are 2 situations which needs to be handled
                if count < k:  # If the number of values missing is still less than required K
                    return nums[mid] + abs(k - count)  # adding the k-count no of values to the last value
                else:  # Else, if count is either greater than or equal to k
                    cnt = MissingElementsCount(nums[0] + mid - 1, nums[mid - 1])
                    return nums[mid - 1] + abs(k - cnt)  # adding k - count of previous term to the previous term of mid
            if count < k:  # If count value is less than k
                low = mid + 1  # updating low value to mid + 1
            else:  # Else if count value is greater than or equal to k
                high = mid - 1  # updating high value to mid - 1
                # At the end the low value will be pointed to the index where count is >= k

        prevCnt = MissingElementsCount(nums[0] + low - 1, nums[low - 1])
        # Hence, calculating the count of previous value to low
        return nums[low - 1] + abs(k - prevCnt)  # and adding k - prevcnt to the previous value.


obj1 = Solution()
assert obj1.missingElement([4, 7, 9, 10], 1) == 5  # TestCase 1
assert obj1.missingElement([4, 7, 9, 10], 3) == 8  # TestCase 2
assert obj1.missingElement([1, 2, 4], 3) == 6  # TestCase 3
assert obj1.missingElement([746421, 1033196, 1647541, 4775111, 7769817, 8030384], 10) == 746431  # TestCase 4
assert obj1.missingElement([1, 2, 10], 3) == 5  # TestCase 5
assert obj1.missingElement([1], 3) == 4  # TestCase 6
