class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        def lower_bound(l, r, target):
            res = len(intervals)
            while l <= r:
                mid = (l+r)//2
                if target < intervals[mid][1]:
                    res = mid
                    r = mid - 1
                else:
                    l = mid + 1
            return res-1

        intervals.sort(key = lambda x: x[1])
        dp = [0]*(len(intervals)+1)
        for i in range(1, len(dp)):
            last = lower_bound(0, i-1, intervals[i-1][0])
            dp[i] = max(dp[i-1], dp[last+1]+1)
        return len(intervals) - dp[-1] 