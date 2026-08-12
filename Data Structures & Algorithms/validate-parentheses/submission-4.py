class Solution:
    def isValid(self, s: str) -> bool:
        chars = []
        for char in s:
            if char == '(' or char == '{' or char == '[' :
                chars.append(char)
            elif char == ')' or char == '}' or char == ']':
                if len(chars) > 0 :
                    if chars[-1] == '(' and char == ')' :
                        chars.pop()
                    elif chars[-1] == '{' and char == '}':
                        chars.pop()
                    elif chars[-1] == '[' and char == ']':
                        chars.pop()
                    else: 
                        return False
                else:
                    return False
                
        if len(chars) == 0 :
            return True
        
        else:
            return False