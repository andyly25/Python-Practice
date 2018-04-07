'''
Sudoku is a number-placement puzzle. The objective is to fill a 9 × 9 grid with 
numbers in such a way that each column, each row, and each of the nine 3 × 3 
sub-grids that compose the grid all contain all of the numbers from 1 to 9 one time.

Implement an algorithm that will check whether the given grid of numbers 
represents a valid Sudoku puzzle according to the layout rules described 
above. Note that the puzzle represented by grid does not have to be solvable.


'''

def checkRow(row):
     tmpDict = {}
     isValid = True

     if len(row) > 0:
          for x in row:
               # check if there's a dupe
               if x in tmpDict:
                    tmpDict[x] += 1
                    # valid = False
                    # break;
               else:
                    tmpDict[x] = 1
          if tmpDict[max(tmpDict, key=tmpDict.get)] > 1:
               isValid = False

     return isValid

def checkGrid(grid):
     isValid = True

     for i in range(len(grid)):
          row = [int(x) for x in grid[i] if x != '.']
          isValid = checkRow(row)
          if not isValid:
               break
     return isValid

def grid3x3Valid(grid):
     isValid = True
     # now we start checking by 3's these will be the start of the rows
     for i in range(0, len(grid), 3):
          if not isValid:
               break
          # we grab the 3 numbers from matrix
          subMatrix = grid[i:i+3]
          # now we start checking by 3's going down the column
          for j in range(0, len(grid[0]), 3):
               # here we form the columns for the submatrix
               tmpList = [x[j:j+3] for x in subMatrix]
               # we now start filling in the numbers for our 3x3 matrix
               tmpList = [tmpList[a][b] for a in range(len(tmpList)) for b in range(len(tmpList[a]))]

               # now we check the numbers in row excluding the '.'
               row = [int(x) for x in tmpList if x!= '.']
               isValid = checkRow(row)
               if not isValid:
                    break
     return isValid


def sudoku2(grid):
     isValid = False
     validRow = checkGrid(grid)
     # similar trick to the rotate matrix in previous challenge
     validCol = checkGrid(list(zip(*grid)))
     valid3x3 = grid3x3Valid(grid)
     # final check if all is true
     if validRow and validCol and valid3x3:
          isValid = True
     return isValid






## takes a square matrix (sudoku) as input, returns T/F for correctness



grid1 = [['.', '.', '.', '.', '2', '.', '.', '9', '.'],
        ['.', '.', '.', '.', '6', '.', '.', '.', '.'],
        ['7', '1', '.', '.', '7', '5', '.', '.', '.'],
        ['.', '7', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '8', '3', '.', '.', '.'],
        ['.', '.', '8', '.', '.', '7', '.', '6', '.'],
        ['.', '.', '.', '.', '.', '2', '.', '.', '.'],
        ['.', '1', '.', '2', '.', '.', '.', '.', '.'],
        ['.', '2', '.', '.', '3', '.', '.', '.', '.']]

grid2 = [['.', '.', '.', '1', '4', '.', '.', '2', '.'],
        ['.', '.', '6', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '1', '.', '.', '.', '.', '.', '.'],
        ['.', '6', '7', '.', '.', '.', '.', '.', '9'],
        ['.', '.', '.', '.', '.', '.', '8', '1', '.'],
        ['.', '3', '.', '.', '.', '.', '.', '.', '6'],
        ['.', '.', '.', '.', '.', '7', '.', '.', '.'],
        ['.', '.', '.', '5', '.', '.', '.', '7', '.']]

print(sudoku2(grid1))
print(sudoku2(grid2))