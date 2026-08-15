class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort( key = lambda x: x[1])
        def get_prev_interval(idx):
            res = -1
            for i in range(idx-1, -1, -1):
                if intervals[idx][0] >= intervals[i][1]:
                    res = i
                    break
            return res

        def get_floor(l, r, target):
            # largest element <= target
            res = -1
            while l<=r:
                mid = (l+r)//2
                if intervals[mid][1] <= target:
                    res = mid
                    l = mid+1
                else:
                    r = mid - 1
            return res
            return res

        dp = [0]*(len(intervals)+1)
        for i in range(1, len(dp)):
            # p = get_prev_interval(i-1)
            p = get_floor(0, i-2, intervals[i-1][0])
            dp[i] = max(dp[i-1], dp[p+1]+1)
        return len(intervals)-dp[-1]