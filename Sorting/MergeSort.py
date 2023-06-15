"""
MergeSort (Divide and conquer): Divide the problem into smaller instances of problems
and solve the smaller instances

Sol: Calculate the mid pointer and call the function recursively
"""

def mergeSort(nums):
    return mergeSortHelper(nums, 0, len(nums)-1)

def mergeSortHelper(nums, start, end):
    if start >= end:
        return nums
    mid = start + (end - start) // 2
    mergeSortHelper(nums, start, mid)
    mergeSortHelper(nums, mid+1, end)
    i = start
    j = mid + 1
    auxArray = []
    while i<=mid and j<=end:
        if nums[i] <= nums[j]:
            auxArray.append(nums[i])
            i += 1
        else:
            auxArray.append(nums[j])
            j += 1

    while i <= mid:
        auxArray.append(nums[i])
        i += 1
    while j <= end:
        auxArray.append(nums[j])
        j += 1
    nums[start:end+1] = auxArray
    return nums


print(mergeSort([ 7, 3, 1, 6, 2, 9]))
print(mergeSort([1, 3, 1, 4, 7, 2, 1, 0]))

#Time Complexity - O(n log n)
"""
Merge sort doesn't have different complexities for best, worst and average cases. It is O(n log n) for all the cases
"""