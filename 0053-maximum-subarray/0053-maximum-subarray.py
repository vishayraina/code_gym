class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = float("-inf")
        sm = 0
        for r in range(len(nums)):
            sm += nums[r]
            res = max(res, sm)
            if sm < 0:
                sm = 0
        return res
            
            