class Solution:
    def isValid(self, s: str) -> bool:
        # Pop elements and push into new stack, check same as 's'
        stack = []
        
        for item in s:
            if item == "(" or item == "[" or item == "{":
                stack.append(item);
            elif not stack:
                return False
            else:
                top = stack[-1]
                if item == ")" and top == "(":
                    stack.pop()
                elif item == "}" and top == "{":
                    stack.pop()
                elif item == "]" and top == "[":
                    stack.pop()
                else:
                    return False
        if not stack:
            return True
        else:
            return False
        

