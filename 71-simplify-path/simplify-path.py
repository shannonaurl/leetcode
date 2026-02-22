class Solution:
    def simplifyPath(self, path: str) -> str:

        # initialize stack = []
        # if length == 1: return "/"
        # loop through the characters in the string from index 1 onwards: 
        # initialize curr_elem = ""
        # while it's not a "/":  
        #      add characters into curr_elem 
        # if curr_elem == ".": 
        #    pop one element from the stack
        # elif curr_elem == "..": 
        #    pop two elements from the stack 
        # else: append curr_elem to stack 

        # stack is done, now construct the simplified string: 
        # output = "/"
        # output.append(stack[0])
        # output.append(stack[i])

        stack = []
        
        if len(path) == 1: return "/"

        l = 1 
        while l < len(path): 
            curr_elem = "" 
            while l < len(path) and path[l] != "/": 
                curr_elem += path[l]
                l += 1 
            if curr_elem == "." or curr_elem == "": 
                l += 1 
                continue 
            elif curr_elem == "..": 
                if stack:
                    stack.pop()
            else: 
                stack.append(curr_elem)
            l += 1 

        return "/" + "/".join(stack)
            

        