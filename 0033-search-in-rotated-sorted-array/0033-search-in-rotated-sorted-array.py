class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def get_pivot():
            left, right = 0, len(nums)-1
            res, resval = len(nums), float("inf")
            while left <= right:
                mid = (left+right)//2
                if nums[mid] <= nums[right]:
                    if resval >= nums[mid]:
                        res = mid
                        resval = nums[res]
                    right = mid -1
                else:
                    left = mid + 1
            return res
        def bs(nums, left, right, target):
            while left <= right:
                mid = (left+right)//2
                if nums[mid] == target:
                    return mid
                elif target < nums[mid]:
                    right = mid -1
                else:
                    left = mid + 1
            return -1
        pivot = get_pivot()
        if nums[pivot] <= target  and target <= nums[-1]:
            return bs(nums, pivot, len(nums)-1, target)

        return  bs(nums, 0, pivot-1, target)
