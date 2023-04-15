class Solution:
    def maxArea(self, height: List[int]) -> int:
        l,r =  0, len(height)-1
        h= max(height)
        res=0
        
        while(l<r):
            res= max(res, min(height[l],height[r])*(r-l))
            
            if (height[l]<=height[r]):
                l+=1
            elif(height[l]>height[r]):
                r-=1
            
            if (r-l)*h < res:
                break
        return res
            
            
            