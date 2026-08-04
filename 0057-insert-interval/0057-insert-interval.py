class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        l, r = 0, len(intervals)-1
        res = len(intervals)
        while l <= r:
            mid = (l+r)//2
            if newInterval[0] <= intervals[mid][0]:
                res = mid
                r = mid-1
            else:
                l = mid+1  
        
        sol = []
        for i in range(res):
            sol.append(intervals[i])
        
        if not sol or sol[-1][1] < newInterval[0]:
            sol.append(newInterval)
        else:
            sol[-1][1] = max(sol[-1][1], newInterval[1])

        for i in range(res, len(intervals)):
            if not sol or sol[-1][1] < intervals[i][0]:
                sol.append(intervals[i])
            else:
                sol[-1][1] = max(sol[-1][1], intervals[i][1])
        return sol



        
