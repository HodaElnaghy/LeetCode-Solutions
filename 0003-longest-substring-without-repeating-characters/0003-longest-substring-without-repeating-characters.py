class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        arr = []
        maxLength = 0
        count = 0
        
        for el in s:
            
            if el in arr:
                arr = arr[arr.index(el)+1:]
                count = len(arr)
            
            arr.append(el)
            count +=1
            
            maxLength = max(count,maxLength)
            
        return maxLength
                
        