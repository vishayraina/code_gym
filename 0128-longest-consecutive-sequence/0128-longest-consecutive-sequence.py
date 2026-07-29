class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hset = set(nums)
        res = 0
        for n in hset:
            if n-1 not in hset:
                cur = 0
                while n in hset:
                    cur += 1
                    res = max(res, cur)
                    n += 1
        return res
                
