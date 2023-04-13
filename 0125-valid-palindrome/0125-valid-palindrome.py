class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        
        l=0
        r=len(s)-1
        while(l<r):
            if (s[l].isalnum() and s[r].isalnum() and s[l]==s[r]):
                l+=1
                r-=1
            elif (s[r].isalnum() == False):
                r-=1
            elif (s[l].isalnum() == False):
                l+=1
            else:
                return False
        return True
        
        
        
        