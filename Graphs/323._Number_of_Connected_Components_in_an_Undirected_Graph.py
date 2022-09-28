"""
You have a graph of n nodes. You are given an integer n and an array edges where edges[i] = [ai, bi]
indicates that there is an edge between ai and bi in the graph.

Return the number of connected components in the graph.
"""
from collections import defaultdict
from collections import deque


class Solution(object):
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        AdjList = defaultdict(list)
        visited = set()
        count = 0
        deq = deque()

        for (u, v) in edges:
            AdjList[u].append(v)
            AdjList[v].append(u)

        def dfs(lis):
            for i in lis:
                if i not in visited:
                    visited.add(i)
                    dfs(AdjList[i])

        for j in range(0,n):
            if j not in visited:
                dfs(AdjList[j])
                visited.add(j)
                count += 1

        def bfs():
            for x in range(0,n):
                if x not in visited:
                    visited.add(x)
                    deq.append(AdjList[x])
                    deq.popleft()

        for j in range(0, n):
            if j not in visited:
                deq.append(j)
                bfs(j)
                visited.add(j)
                count += 1

        return count


obj1 = Solution()
print(obj1.countComponents(5, [[0, 1], [1, 2], [3, 4]]))
print(obj1.countComponents(5, [[0, 1], [1, 2], [2, 3], [3, 4]]))
