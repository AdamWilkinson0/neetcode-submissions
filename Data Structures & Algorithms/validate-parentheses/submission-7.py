class Solution:
    def isValid(self, s: str) -> bool:
        opens = {'{','[','('}
        stack = []
        for i in range(len(s)):
            if stack:
                top = stack[-1]
            if s[i] in opens:
                stack.append(s[i])
            else:
                if stack:
                    top = stack[-1]
                    if s[i] == '}' and top == '{':
                        stack.pop()
                    elif s[i] == ']' and top == '[':
                        stack.pop()
                    elif s[i] == ')' and top == '(':
                        stack.pop()
                    else:
                        return False
                else:
                    return False
        if not stack:
            return True
        else:
            return False


        

        
        

