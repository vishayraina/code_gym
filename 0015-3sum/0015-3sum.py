class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        def twoSum(l, r, target):
            sol = []
            while l < r:
                if nums[l] + nums[r] > target:
                    r -= 1
                elif nums[l] + nums[r] < target:
                    l += 1
                else:
                    sol.append([nums[l], -target, nums[r]])
                    l += 1
                    while l < len(nums) and nums[l-1] == nums[l]:
                        l += 1
                    r -= 1
            return sol
        res = []
        for i in range(len(nums)):
            if i > 0 and nums[i-1] == nums[i]:
                continue
            res.extend(twoSum(i+1, len(nums)-1, -nums[i]))
        return res