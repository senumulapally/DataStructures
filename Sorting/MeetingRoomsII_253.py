"""
Given an array of meeting time intervals intervals where intervals[i] = [starti, endi],
return the minimum number of conference rooms required.

Example 1:
Input: intervals = [[0,30],[5,10],[15,20]]
Output: 2

Example 2:
Input: intervals = [[7,10],[2,4]]
Output: 1

Sol:  Sort both the start and end arrays separately. Similar to merge sort keep traversing both arrays
when start<end increment start+1 and increase the currentCount of conf rooms by 1 else, increment end+1
and decrement the conf rooms currCount-1. Keep updating the max count of conf rooms at the end of every loop.
By the end of loop  we will get the max count of conf rooms required.
"""


# Correct Solution
class Solution1(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        start_numbers = sorted([interval[0] for interval in intervals])
        end_numbers = sorted([interval[1] for interval in intervals])
        l = len(intervals)
        start, end = 0, 0
        currCount, count = 0, 0
        while start < l:
            if start_numbers[start] < end_numbers[end]:
                start += 1
                currCount += 1
            else:
                end += 1
                currCount -= 1
            count = max(currCount, count)
        return count


# Time Complexity O(n log n) [for sorting it takes O(n log n) time, and for loop it taxes max of 2n iterations]

obj = Solution1()
print(obj.minMeetingRooms([[4, 10], [2, 4]]))
print(obj.minMeetingRooms([[0, 30], [5, 10], [15, 20]]))


# BruteForce - Not working
class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        # intervals = sorted(intervals, key=lambda x: x[0])
        l = len(intervals)
        count = 0
        dic = dict()
        for i in range(l):
            currCount = 0
            for j in range(i, l):
                if intervals[i][1] > intervals[j][0]:
                    currCount += 1
            count = max(currCount, count)
        return count
