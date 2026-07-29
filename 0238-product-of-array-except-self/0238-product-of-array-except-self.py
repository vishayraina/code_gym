class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        prev = 1
        for i in range(len(nums)):
            prefix.append(prev)
            prev *= nums[i]
        
        prev = 1
        res = [0]*len(nums)
        for i in range(len(nums)-1, -1, -1):
            res[i] = prefix[i] * prev
            prev *= nums[i]
        return res