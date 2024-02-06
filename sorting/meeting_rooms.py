# Given an array of meeting time intervals consisting of start and end times[[s1,e1],[s2,e2],...](si< ei),
# determine if a person could attend all meetings
# Input:
# [[5,10], [0,30],[15,20]]
# Output: false
# Input:[[7,10],[2,4]]
# Output:true
from typing import List


def meeting_rooms(arr: List[List[int]]) -> bool:
    # First sort the start times in asc order
    sorted_meetings = sorted(arr, key=lambda x: x[0])
    # Need a tmp variable to store the previous meeting's end time
    last_end = -1
    # Iterate and check if the end time of previous meeting overlaps (>=) with the start time of the next meeting
    for start, end in sorted_meetings:
        if start <= last_end:
            return False
        last_end = end
    return True


test_meeting = [[7, 10], [2, 4]]
print(test_meeting)
print('....................')
print("Can attend all meetings ?, Ans = ", meeting_rooms(test_meeting))

test_meeting = [[5, 10], [0, 30], [15, 20]]
print(test_meeting)
print('....................')
print("Can attend all meetings ?, Ans = ", meeting_rooms(test_meeting))
