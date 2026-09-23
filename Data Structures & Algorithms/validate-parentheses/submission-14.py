class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closingChars = {')', '}', ']'}   
        pairs = {'(':')', '{':'}', '[':']'}     

        for i in range(len(s)):
            if s[i] not in closingChars:
                stack.append(s[i])
            else:
                if not stack:
                    return False
                elif s[i] != pairs[stack[-1]]:
                    return False
                else:
                    stack.pop()
        
        if not stack:
            return True
        else:
            return False