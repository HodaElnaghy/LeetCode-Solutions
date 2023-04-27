class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hash_table = {')':'(',
                     '}':'{',
                     ']':'['
                     }
        
        for el in s:
            if (el not in hash_table):
                stack.append(el)
                continue
            if (stack and stack[-1] == hash_table[el]):
                stack.pop()
            else:
                return False
                
        if stack:
            return False
        else:
            return True
        