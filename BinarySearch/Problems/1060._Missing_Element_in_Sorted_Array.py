class Solution(object):
    def missingElement(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        low = 0
        high = len(nums)-1
        while low <= high:
            mid = low + (high - low) // 2
            if nums[0]+mid != nums[mid]:
                for j in range(nums[i-1]+1, nums[i]):
                    arr.append(j)
        m = len(arr)
        last = arr[m-1]
        if k > m:
            while m < k:
                last += 1
                arr.append(last)
                m += 1


        return arr

    def MissingElements(self, val1, val2):





obj1 = Solution()
print(obj1.missingElement([4, 7, 9, 10], 1))
print(obj1.missingElement([4, 7, 9, 10], 3))
print(obj1.missingElement([1, 2, 4], 3))
