class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def get_pivot():
            l, r = 0, len(nums)-1
            res = len(nums)
            mn = float("inf")
            while l <= r:
                mid = (l+r)//2
                if nums[mid] <= nums[r]:
                    if nums[mid] < mn:
                        res = mid
                        mn = nums[res]
                    r = mid - 1
                else:
                    l = mid + 1
            return res
        def binary_search(l, r):
            while l <= r:
                mid = (l+r)//2
                if target == nums[mid]:
                    return mid
                elif target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            return -1
        pivot = get_pivot()
        if target >= nums[pivot] and target <= nums[len(nums)-1]:
            return binary_search(pivot, len(nums)-1)
        else:
            return binary_search(0, pivot-1)
         
