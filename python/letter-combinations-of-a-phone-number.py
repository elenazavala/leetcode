class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # Backtracking Tree Solution 
        # * see notebook for visual image and long explanation: 
        
        
        #Backtracking is about:
        # 1. The choices we make
        # 2. Our constraints ( we dont have in this problem )
        # 3. And our goal
        
        res = []
        digitmap = { "2" : "abc",
                     "3" : "def",
                     "4" : "ghi",
                     "5" : "jkl",
                     "6" : "mno",
                     "7" : "qprs",
                     "8" : "tuv",
                     "9" : "wxyz" }
        
        def backtrack(i, curStr):
            '''
            params: -> i will give us where we are at in our digits input string ex = "23"
                    -> curStr is the string we are building to append to our result
            ''' 
            #our goal
            if len(curStr) == len(digits):
                res.append(curStr)
                return
            
            #choices
            for char in digitmap[digits[i]]:
                backtrack(i + 1, curStr + char)
        
        if digits: #if its non empty
            backtrack(0, "")
        return res
       
        #note 1:
        # digits = 23
        # digits[0] = 2 and digits[1] = 3
        # digitmap[digits[0]] = "abc" since digits[0] is 2.. this is our key
        # digitmap[digits[1]] = "def" since digits[1] is 3.. this is our key
