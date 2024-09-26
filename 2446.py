# https://leetcode.com/problems/determine-if-two-events-have-conflict/description/

'''

You are given two arrays of strings that represent two inclusive events that happened on the same day, event1 and event2, where:

event1 = [startTime1, endTime1] and
event2 = [startTime2, endTime2].
Event times are valid 24 hours format in the form of HH:MM.

A conflict happens when two events have some non-empty intersection (i.e., some moment is common to both events).

Return true if there is a conflict between two events. Otherwise, return false.

test case :- 
Example 1:

Input: event1 = ["01:15","02:00"], event2 = ["02:00","03:00"]
Output: true
Explanation: The two events intersect at time 2:00.
Example 2:

Input: event1 = ["01:00","02:00"], event2 = ["01:20","03:00"]
Output: true
Explanation: The two events intersect starting from 01:20 to 02:00.
Example 3:

Input: event1 = ["10:00","11:00"], event2 = ["14:00","15:00"]
Output: false
Explanation: The two events do not intersect.

'''


class Solution:
    def haveConflict(self, event1: List[str], event2: List[str]) -> bool:
        def convert_to_minutes(time_str):
            hours, minutes = map(int, time_str.split(":"))
            return hours * 60 + minutes
        
        start1 = convert_to_minutes(event1[0])
        end1 = convert_to_minutes(event1[1])
        start2 = convert_to_minutes(event2[0])
        end2 = convert_to_minutes(event2[1])
        
        
        return start1 <= end2 and start2 <= end1


