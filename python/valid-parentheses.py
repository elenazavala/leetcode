class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        map = { ")":"(" , "]":"[" , "}":"{"} #maps close to open parenthesis
        stack = [] #stack of open parenthesis
        
        for bracket in s:
            if bracket in map:  # If its an CLOSING bracket (cause our keys to map are closing brackets) 
                
                if stack and (stack[-1] == map[bracket]): # If top of stack, which is the opening bracket matches the closing bracket correctly
                    stack.pop() # Pop opening bracket form stack
                
                else: # If they do not match correctly
                    return False
                
            else: #If its an OPENING bracket
                stack.append(bracket)
                
        # if stack is empty it means all of our brackets matched correctly so we return true, otherwise we return false
        
        if not stack:
            return True
        else:
            return False
