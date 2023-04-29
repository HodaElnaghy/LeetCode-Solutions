class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums)-1
        
        while high >= low:
            mid = (high+low)//2
            if nums[mid] == target:
                return mid 
            
            elif nums[mid]< nums[low]:
                if target > nums[mid] and target <= nums[high]:
                    low = mid+1
                else:
                    high = mid-1
            else :
                if target >=nums[low] and target <nums[mid]:
                    high= mid-1
                else:
                    low = mid+1
                
                 
                
            
            
                    
        return -1
                
        