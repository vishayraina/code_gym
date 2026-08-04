class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # need last non overlapping interval p[i] for each interval i
        # i.e., p[i][1] <= intervals[i][0]
        # i.e., the largest end time that is less than current interval start time. lowerbound + 1

        # dp[n] = max(dp[n-1], dp[p[n]]+1)

        # dp[n] := max non overlapping intervals given the first n intervals
        intervals.sort(key = lambda x: x[1])
        def p(i):
            l, r = 0, i-1
            target = intervals[i][0]
            res = i
            while l <= r:
                mid = (l+r)//2
                if target < intervals[mid][1]:
                    res = mid
                    r = mid - 1
                else:
                    l = mid + 1
            return res

        dp = [0] * (len(intervals)+1)
        for i in range(1, len(dp)):
            dp[i] = max(dp[i-1], dp[p(i-1)]+1)
        return  len(intervals) - dp[-1]

            