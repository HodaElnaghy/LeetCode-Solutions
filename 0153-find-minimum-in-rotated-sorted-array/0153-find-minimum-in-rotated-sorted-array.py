class Solution:
    def findMin(self, nums: List[int]) -> int:
        low = 0
        high = len(nums)-1
        res = nums[0]
        while high>=low:
            mid = (high+low)//2
            res = min(nums[mid],res)
            if nums[low]<nums[high]:
                return min(nums[low],res)
            elif nums[mid] >= nums[low] and mid+1<=len(nums)-1:
                low = mid+1
            else:
                high = mid -1
        return res
            