class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        nums = set(nums)
        mn, mx = min(nums), max(nums)
        res = []
        for i in range(mn, mx+1):
            if i not in nums:
                res.append(i)
        return res