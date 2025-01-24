"""
Leetcode 207
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1.
You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course
bi first if you want to take course ai.
For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.

Example 1:
Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take.
To take course 1 you should have finished course 0. So it is possible.

Example 2:
Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take.
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.
"""
from typing import List, Set


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visited: List[int] = [-1] * numCourses
        adj_list: List[Set[int]] = [set() for _ in range(numCourses)]
        for crs,pre in prerequisites:
            adj_list[pre].add(crs)
        timestamp: List[int] = [0]
        arr: List[int] = [-1] * numCourses
        dep: List[int] = [-1] * numCourses

        def dfs(root: int):
            visited[root] = 1
            arr[root] = timestamp[0]
            timestamp[0] += 1
            for nbr in adj_list[root]:
                if visited[nbr] != 1:
                    if dfs(nbr) == False:
                        return False
                else:
                    if dep[nbr] == -1:
                        return False
                    # elif arr[nbr] < arr[root]  and departure time is set then it is a cross edge
                    # elif arr[nbr] > arr[root] and departure time is set, then it is a forward edge
            dep[root] = timestamp[0]
            timestamp[0] += 1
            return True

        for crs in range(numCourses):
            if visited[crs] != 1:
                can_fin: bool = dfs(crs)
                if not can_fin:
                    return False
        return True

sol = Solution()
numCourses = 2
prerequisites = [[1,0]]
print("sol:", sol.canFinish(numCourses, prerequisites))

numCourses = 2
prerequisites = [[1,0],[0,1]]
print("sol:", sol.canFinish(numCourses, prerequisites))
