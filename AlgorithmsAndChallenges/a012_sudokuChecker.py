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



# ---------------------------
# Here's another person's solution
def check_unique(nums):
     s = set()
     for num in nums:
          if num == '.':
               continue 
            
          if num in s:
               return False
          s.add(num)
     return True
        

def sudoku3(grid):
     for line in grid:
          if not check_unique(line):
               return False
    
     for i in range(9):
          if not check_unique([line[i] for line in grid]):
               return False
        
     for i in range(0,9,3):
          for j in range(0, 9, 3):
               if not check_unique(grid[i][j:j+3] + grid[i+1][j:j+3] + grid[i+2][j:j+3]):
                    return False
            
     return True


#-------
# Here's another in python2
# originally had xrange, changed to range
# and the zip used didn't have list before it
# list indices must be integers or slices, not float, so we use // instead of /
# Thank you stack overflow for pointing differences between python2 and 3!
def sudoku4(grid):
     def unique(G):
          G = [x for x in G if x != '.']
          return len(set(G)) == len(G)
     def groups(A):
          B = list(zip(*A))
          for v in range(9):
               yield A[v]
               yield B[v]
               yield [A[v//3*3 + r][v%3*3 +c] 
                    for r in range(3) for c in range(3)]
    
     return all(unique(grp) for grp in groups(grid))

# -------------
# last one
def sudoku5(grid):
     for i in range(9):
          for j in range(9):
               num = grid[i][j]
               if num != '.':
                    for k in range(9):
                         if k != j and grid[i][k] == num:
                              return False
                         if k != i and grid[k][j] == num:
                              return False
                         top_i = i - i%3
                         top_j = j - j%3
                         if (top_i+k//3,top_j+k%3) != (i,j) and grid[top_i+k//3][top_j+k%3] == num:
                              return False

     return True
                





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
print(sudoku4(grid1))
print(sudoku4(grid2))