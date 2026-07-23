class Solution:
    def search(self, nums: List[int], target: int) -> int:

        def binarysearch(low, high):
            if low > high:
                return -1

            mid = (low + high) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                return binarysearch(mid + 1, high)
            else:
                return binarysearch(low, mid - 1)

        return binarysearch(0, len(nums) - 1)