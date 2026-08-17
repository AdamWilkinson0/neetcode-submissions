class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        lowerS = s.lower()
        chars = list(lowerS)
        chars = [char for char in chars if char.isalnum()]
        
        if not chars:
            return True

        lp = 0
        rp = len(chars)-1
        while lp <= (len(chars)/2):
            if chars[lp] != chars[rp]:
                return False
            lp += 1
            rp -= 1
        return True
        