class Solution:
    def isValid(self, s: str) -> bool:

        # traverse through the string: 
        # if see open bracket, add to stack 
        # else (u see a closed bracket): if stack (edge case 1: starting is a close bracket): check if elem = pairs[stack.pop()], if doesn't match == return False 

        # if stack: return False # edge case 1: there is an open bracket left unsealed 

        pairs = {"{": "}", "(": ")", "[": "]"} 

        stack = []
        for i in range(len(s)): 
            if s[i] in pairs: 
                stack.append(s[i])
            else: 
                if stack and s[i] == pairs[stack.pop()]: 
                    continue  
                else: 
                    return False 
        
        return not stack 
        