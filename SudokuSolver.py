# Fill the chart below according to your onw sudoku.
# Write "0" to replace empty spaces! 
sudoku = [[8,0,0,2,0,0,0,0,0],
          [0,0,0,0,0,9,0,1,0],
          [3,4,5,0,0,0,0,0,0],
          [0,0,0,1,0,0,0,5,0],
          [0,6,0,0,0,0,0,0,3],
          [0,3,8,7,0,0,2,9,0],
          [0,1,0,0,0,0,0,0,6],
          [0,0,7,9,0,0,0,2,0],
          [0,0,0,0,0,3,0,0,0],            
        ]

def is_valid(row, col, guess):
    
    row_numbers = sudoku[row]
    if guess in row_numbers:
        return False

    for i in range(9):
        if sudoku[i][col] == guess:
            return False
    
    row_start = (row // 3) * 3
    col_start = (col // 3) * 3
    
    for x in range(row_start, row_start + 3):
        for y in range(col_start, col_start + 3):
            if sudoku[x][y] == guess:
                return False
    
    return True