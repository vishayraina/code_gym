class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # find insert position
        l, r = 0, len(intervals)-1
        res = len(intervals)
        while l <= r:
            mid = (l+r)//2
            if newInterval[0] <= intervals[mid][0]:
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        
        intervals.insert(res, newInterval)
        
        res = []
        for i in range(len(intervals)):
            if not res or res[-1][1] < intervals[i][0]:
                res.append(intervals[i])
            else:
                res[-1][1] = max(res[-1][1], intervals[i][1])
        return res


        
