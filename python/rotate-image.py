import numpy as np
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # Brute Force, Double for loop
        # [2][0] [1][0] [0][0] , [2][1] [1][1] [0][1] , [2][2] [1][2] [0][2]

        m = 0
        l = len(matrix[0]) - 1
        reset = l
        x = np.array(matrix)
        copy = x.view()

        for i in range(len(matrix)):
            if l < 0 or m > l:
                    l = reset
                    m += 1
            for j in range (len(matrix)):
                print("new i val:", l, "new j val:", m)
                matrix[i][j] = copy[l][m]
                l -= 1
