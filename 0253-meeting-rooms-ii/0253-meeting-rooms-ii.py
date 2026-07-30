import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x:x[0])
        heap = []
        res = 0
        for i in range(len(intervals)):
            if not heap or heap[0] > intervals[i][0]:
                heapq.heappush(heap, intervals[i][1])
                res += 1
            else:
                heapq.heappop(heap)
                heapq.heappush(heap, intervals[i][1])
        return res