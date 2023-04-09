class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        CountS, CountT = {}, {}
        for i in range(len(s)):
            if s[i] in CountS:
                CountS[s[i]] += 1
            else:
                CountS[s[i]] = 1
            CountT[t[i]] = 1 + CountT.get(t[i], 0)
        return CountS == CountT