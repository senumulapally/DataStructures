"""Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k,
return the k closest points to the origin (0, 0).
The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).
You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).

Example 1:
Input: points = [[1,3],[-2,2]], k = 1
Output: [[-2,2]]
Explanation:
The distance between (1, 3) and the origin is sqrt(10).
The distance between (-2, 2) and the origin is sqrt(8).
Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
We only want the closest k = 1 points from the origin, so the answer is just [[-2,2]].

Example 2:
Input: points = [[3,3],[5,-1],[-2,4]], k = 2
Output: [[3,3],[-2,4]]
Explanation: The answer [[-2,4],[3,3]] would also be accepted.

Sol: Quick Select pattern - Select a pivot and loop it to get smaller elements on left and bigger elements on right
at the end check if pivot element's index is equal to required Kth element. If yes, return all the elements from 0-k
else if pivot element's index id smaller than required index,
 recursively execute the method for left partition else continue it for right partition
"""
import random


class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        l = len(points)
        if l <= 0 or k <= 0:
            return None
        if k == l:
            return points
        return self.kClosestHelper(points, k, 0, l - 1)

    def kClosestHelper(self, points, k, start, end):
        randIndex = random.randint(start, end)
        # pivot = point[randIndex]
        pivotDist = (points[randIndex][0] ** 2) + (points[randIndex][1] ** 2)
        points[randIndex], points[start] = points[start], points[randIndex]
        smaller = start
        for bigger in range(start + 1, end + 1):
            dist = points[bigger][0] ** 2 + points[bigger][1] ** 2
            if dist < pivotDist:
                smaller += 1
                points[bigger], points[smaller] = points[smaller], points[bigger]

        points[start], points[smaller] = points[smaller], points[start]
        if smaller == k:
            return points[:k]
        elif smaller > k:
            return self.kClosestHelper(points, k, start, smaller - 1)
        else:
            return self.kClosestHelper(points, k, smaller + 1, end)


obj = Solution()
print(obj.kClosest([[0,1],[1,0]], 2))
print(obj.kClosest([[-5,4],[-6,-5],[4,6]], 2))
print(obj.kClosest([[1, 3], [-2, 2]], 1))
print(obj.kClosest([[3, 3], [5, -1], [-2, 4]], 2))
