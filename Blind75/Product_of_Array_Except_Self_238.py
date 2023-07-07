"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product
of all the elements of nums except nums[i].
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
You must write an algorithm that runs in O(n) time and without using the division operation.

Example 1:
Input: nums = [1,2,3,4]
Output: [24,12,8,6]
op[0] = 2*3*4
op[1] = 1*3*4
op[2] = 1*2*4
op[3] = 1*2*3

Example 2:
Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]

Sol: traverse from left to right and keep track of multiplication
of its previous elements and assign them to the result array.
Do the same while traversing from right to left and multiply the values to the already present results. and return the result array

Eg: nums: [1,2,3,4], res array: [1,1,1,1]
leftMul array: [1,1,2,6] -
1 will be as is,
2nd index val from res will be multiplied with 1 from nums
3rd index val of res will be multiplied with 1*2
4th - 1*2*3 = 6
rightMul array:
6 will be as is,
2nd index val will be multiplied with 4,
1 will be miltiplied with 4*3,
first 1 will be multiplied with 2*3*4
"""
#Actual Sol: O(n) Time, O(1) space when return array space is not considered
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = [1] * (len(nums))
        rMul, lMul = 1, 1
        for i in range(0,len(nums)):
            res[i] = rMul
            rMul = rMul*nums[i]

        for i in range (len(nums)-1, -1, -1):
            res[i] *= lMul
            lMul = lMul*nums[i]
        return res


obj = Solution()
print(obj.productExceptSelf([1, 2, 3, 4]))
print(obj.productExceptSelf([-1, 1, 0, -3, 3]))
print(obj.productExceptSelf([0, 1, 2]))

#Brute force O(n sq)
class Solution1(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        for i in range(0, len(nums)):
            res.append(1)
            for j in range(0, len(nums)):
                if j != i:
                    res[i] *= nums[j]
        return res


# obj = Solution()
# print(obj.productExceptSelf([1, 2, 3, 4]))
# print(obj.productExceptSelf([-1, 1, 0, -3, 3]))
# print(obj.productExceptSelf([0, 1, 2]))
