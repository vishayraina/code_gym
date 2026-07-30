class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort(key=lambda x:x[0])
        prev = None
        for i in range(len(intervals)):
            if prev != None and intervals[i][0] < prev[1]:
                return False
            prev = intervals[i]
        return True