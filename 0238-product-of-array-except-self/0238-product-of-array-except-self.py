class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [0]*len(nums)
        prev = 1
        for i in range(len(nums)):
            res[i] = prev
            prev *= nums[i]
        
        prev = 1
        
        for i in range(len(nums)-1, -1, -1):
            res[i] = res[i] * prev
            prev *= nums[i]
        return res