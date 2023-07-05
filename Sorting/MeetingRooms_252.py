"""
Given an array of meeting time intervals where intervals[i] = [starti, endi],
determine if a person could attend all meetings.

Example 1:
Input: intervals = [[0,30],[5,10],[15,20]]
Output: false

Example 2:
Input: intervals = [[7,10],[2,4]]
Output: true

Sol: Sort array based on start values and
later check if start of each interval is greater than end of previous interval
stop and return false whenever there is a conflict
"""

# Actual solution
class Solution1(object):
    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: bool
        """
        intervals = sorted(intervals)
        # Or  you can also write # intervals = sorted(intervals, key=lambda x:x[0])
        l = len(intervals)
        for i in range(0,l-1):
            y = i+1
            if intervals[i][1] > intervals[y][0]:
                return False
        return True


# Trying just for fun
class Solution2:
    def canAttendMeetings(self, intervals):
        counts = set()

        for interval in intervals:
            for i in range(interval[0], interval[1]):
                if i not in counts:
                    counts.add(i)
                else:
                    return False
        return True

obj = Solution1()
print(obj.canAttendMeetings([[4,10],[2,4]]))
print(obj.canAttendMeetings([[0,30],[5,10],[15,20]]))