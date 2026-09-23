class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 1
        biggest = 0
        if not s:
            return 0
        elif len(s) == 1:
            return 1
        window = set()
        window.add(s[l])
        for i in range(len(s)-1):
            
            while s[r] in window and l<r:
                window.remove(s[l])
                l+=1
                window.add(s[l])
            r+=1
            window.add(s[r-1])
            

            size = r-l
            if size > biggest:
                biggest = size
        
        return biggest

