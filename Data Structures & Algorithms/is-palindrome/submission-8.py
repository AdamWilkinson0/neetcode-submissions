class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1


        s = "".join(c for c in s if c.isalnum()).lower()
        return s == s[::-1] 

        while l < r:
            if s[l] != s[r]:
                return False
            else:
                l+=1
                r-=1

        return True
