class Solution:
    
    def isValid(self, s):
        # Fill this in.
        open_par = ["(", "{", "["]
        close_par = [")", "}", "]"] 
        stack = []

        # traverse the string  
        for char in s:
            # if it's an opening parenthesis
            if char in open_par:  
                # push the element in the stack 
                stack.append(char) 
            # if current character is not opening bracket, then it must be closing.  
            else: 
                # if stack is empty
                if not stack: 
                    return False
                current_char = stack.pop() 
                if current_char in open_par: 
                    if char != close_par[open_par.index(current_char)]: 
                        return False
        # after eliminating all opened and closed parentheses
        # the stack shouldn't be empty
        if stack: 
            return False
        return True   

# Test Program
s = "()(){(())" 
# should return False
print(Solution().isValid(s))

s = ""
# should return True
print(Solution().isValid(s))

s = "([{}])()"
# should return True
print(Solution().isValid(s))