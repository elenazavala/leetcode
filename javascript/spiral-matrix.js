/**
 * @param {number[][]} matrix
 * @return {number[]}
 */
var spiralOrder = function(matrix) {
    const res = []
    let start_row = 0, start_col = 0, end_row = matrix.length-1, end_col = matrix[0].length-1;
    
    while(res.length < matrix.length * matrix[0].length) {
        
        for(let col = start_col; col <= end_col; col++ ) {
            res.push(matrix[start_row][col])
        }
        
        for(let row = start_row + 1; row <= end_row; row++) {
            res.push(matrix[row][end_col])
        }
        
        for(let col = end_col - 1; col >= start_col; col--) {
            if(start_row === end_row) break;
            res.push(matrix[end_row][col])
        }
        
        for(let row = end_row - 1; row >= start_row + 1; row--) {
            if(end_col === start_col) break;
            res.push(matrix[row][start_col])
        }
        
        start_row++
        end_row--
        
        start_col++
        end_col--
    }
    
    return res
};
