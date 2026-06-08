class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        if len(s) == 0:
            return True
        elif s[0] == '}' or s[0] == ')' or s[0] == ']':
            return False
        else:
            stack.append(s[0])
        values = {']': '[', ')': '(', '}': '{' }
        
        for i in range(1, len(s)):
            if s[i] == '(' or s[i] == '{' or s[i] == '[':
                stack.append(s[i])
            elif len(stack) == 0:
                return False
            else:
                if stack[-1] == values[s[i]]:
                    del stack[-1]
                else:
                    return False
        if len(stack) == 0:
            return True
        else:
            return False


        