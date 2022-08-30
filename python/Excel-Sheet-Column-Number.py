class Solution:
    def titleToNumber(self, s: str) -> int:
        # alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        if len(s) == 0:
            return 0
        
  
        solution = 0
        for i in range(len(s)):
            solution += ((ord(s[i])-64) * pow(26,len(s)-1-i))
        
        return solution
        
