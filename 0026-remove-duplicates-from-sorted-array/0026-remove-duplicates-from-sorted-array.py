class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        prev = None
        l = 0
        for r in range(len(nums)):
            if nums[r] != prev:
                prev = nums[r]
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
        return l
                