"""
252. Meeting Rooms
Given an array of meeting time intervals where intervals[i] = [starti, endi],
determine if a person could attend all meetings

Example 1:
Input: intervals = [[0,30],[5,10],[15,20]]
Output: false

Example 2:
Input: intervals = [[7,10],[2,4]]
Output: true
"""
from typing import List


class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        # First sort the start times in asc order
        sorted_meetings = sorted(intervals, key=lambda x: x[0])
        # Need a tmp variable to store the previous meeting's end time
        last_end = -1
        # Iterate and check if the end time of previous meeting overlaps (>=) with the start time of the next meeting
        for start, end in sorted_meetings:
            if start <= last_end:
                return False
            last_end = end
        return True


sol = Solution()

meeting_1 = [[7, 10], [2, 4]]
print('....................')
print("meetings:", meeting_1)
print("sol:", sol.canAttendMeetings(meeting_1))

meeting_2 = [[5, 10], [0, 30], [15, 20]]
print('....................')
print("meetings:", meeting_2)
print("sol:", sol.canAttendMeetings(meeting_2))
