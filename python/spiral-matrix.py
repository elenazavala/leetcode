class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        #difficult problem... need to do code by hand to fully understand it
        
        # go right right right
        # down down down
        # up until we couldnt anymore
        
        #  1  2  3  4
        #  5  6  7  8
        #  9 10 11 12
        
        # this is when we finish first spiral and we shrunk the thing
        # now we do the same algorithm with the smaller rectangle
        #  X  X  X  X
        #  X  6  7  X
        #  X  X  X  X
        
        # We are going to have top,left,right,bottom boundaries and keep moving them accordingly
        # i.e when we finish first row, our top boundary [0][0] will go [1][0]
        # similarily, when we rinish rightmost ROW, we shift our right pointer to the left, as we are done with that row
        # and we have a "new boundary"
        
        # So in summary, each time we are done with a row, we shift either our top/bottom boundary
        # and once we are done with a column, we shift either a right/left boundary accordingly
        
        
        # This way,  once our left boundary reaches our right boundary 
        # and our top boundary reaches our bottom boundary it means we have reached the condition to stop
        
        res = []
        cols = len(matrix[0]) #columns
        rows = len(matrix)
        left, right = 0, cols
        top, bottom = 0, rows
        
        while left < right and top < bottom:
            # get every i/value in the top row
            for i in range(left,right): #right value is non inclusive, meaning that if right = 4 it will go from 0,3
                res.append(matrix[top][i]) #si vamos moviendo por columnas, esa es nuestra i
            top += 1 # we've completed top row, so let's update top to one spot down
            
            #get every i/value in the rightmost column
            for i in range(top, bottom): #from TOP to bottom as we've shifted one down (our top pointer)
                res.append(matrix[i][right - 1]) #si vamos moviendo por rows, esa es nuestra i, also our right is technically out of bounds so do -1
            right -= 1 #same shit as top
            
            
            if not (left < right and top < bottom):
                break # if we had a single row or column matrix
                
            #get every i/value in the last row
            for i in range(right - 1, left - 1, -1): #left is non inclusive, do -1 to do it in reverse order
                res.append(matrix[bottom - 1][i])
            bottom -= 1#finished last row, so update our bottom
            
            #get every i/value in the leftmost column
            for i in range(bottom - 1, top - 1, -1): #do -1 to do it in reverse order
                res.append(matrix[i][left])
            left += 1 #finished leftmost row, so update our bottom
