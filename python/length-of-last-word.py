class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        i = len(s) - 1 #pointer to start at the end of the string
        length = 0
        
        # words = s.split()
        
        
        #skip whitespaces
        while s[i] == " ":
            i = i-1
        while i >= 0 and  s[i] != " ": #if we don't put i>=0 entonces el pointer nunca va a terminar de ir a la izda
            
            length = length + 1
            i = i - 1
            
        return length
