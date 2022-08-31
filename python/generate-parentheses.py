class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # Backtracking
        # 1. Choice
        #       place a "(" or a ")"
        #
        # 2. Constraints
        #       we cannot close until we open.
        #           hence we can only place a closing bracket if nopen < nclose
        #               if nopen < nclose while we still have remaining
        #               opening brackets to place (nopen > 0) we will have two choices, 
        #               to close or to open (see link for better understanding)
        #       count of remaining opening parenthesis matter
        #
        # 3. Goal
        #       have n*2 placements. where n is the input, and 2 is how 
        #       if our n is 3 then we will get 6 possible combinations of parenthesis
        # Space complexity = O(n) 
        # Time complexity = fairly rigurous to figure out lol
        
        if n <= 0:
            return []
        res = []
        curStr = ''
       
        def backtrack(nopen, nclose, curStr):
            #goal(base case)
            if nopen == 0 and nclose == 0:
                res.append(curStr)
                return

            #constraints
            if nopen == nclose:
                backtrack(nopen-1, nclose, curStr+'(')  #choice: place an opening bracket

            elif nopen < nclose and nopen > 0: # two choices
                backtrack(nopen-1, nclose, curStr+'(') #choice: place an opening bracket
                backtrack(nopen, nclose-1, curStr+')') #choice: place a closing bracket

            else: # nopen == 0:
                backtrack(nopen, nclose-1, curStr+')') # choice: no more opening parentheses left so we gotta close'em all
        
        backtrack(n,n,'')
        return res
