class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        dictS = {}
        for i in range(len(s)):
            if s[i] in dictS:
                dictS[s[i]] += 1
            else:
                dictS[s[i]] = 1

        dictT = {}
        for i in range(len(t)):
            if t[i] in dictT:
                dictT[t[i]] += 1
            else:
                dictT[t[i]] = 1

        if dictS == dictT:
            return True
        else:
            return False
        

            
        