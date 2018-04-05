
'''
Note: Try to solve this task in-place (with O(1) additional memory), since this is what you'll be asked to do during an interview.

You are given an n x n 2D matrix that represents an image. Rotate the image by 90 degrees (clockwise).

For

a = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
the output should be

rotateImage(a) =
    [[7, 4, 1],
     [8, 5, 2],
     [9, 6, 3]]

Guaranteed constraints:
1 ≤ a.length ≤ 100,
a[i].length = a.length,
1 ≤ a[i][j] ≤ 10^4

def rotateImage(a):
    if a is None or len(a)<1:

'''
def rotateImage(a):
    rows = len(a)
    cols = len(a[0])
    # create a new matrix to store solution     
    rotatedImg = [row[:] for row in a]
    # go along the rows
    for x in range(0, rows):
        # go along the column
        for y in range(0,cols):
            # top of column num will go to end of the row and continues
            rotatedImg[y][rows-x-1] = a[x][y]
    return rotatedImg

# Wow, this is someone's solution, so short
'''
from what I can see we are making a new list by first using
zip: This function takes some equal-length collections, and merges them together
and we do it on *reversed of matrix
[["x","y","z"],
 [ 1,  2,  3],
 ["a","b","c"]]
The * operator can be used in conjuncton with zip() to unzip the list.
makes it:['x', 'y', 'z'], [1, 2, 3], ['a', 'b', 'c']
this then takes the x,1,a and zip that in for our 1st row and continues downwards
'''
def rotateImage2(a):
    return list(zip(*reversed(a)))

# Here's another solution
def rotateImage3(a):
    return [[x[i] for x in a][::-1] for i in range(len(a))]



if __name__=="__main__":
    six = [["a","b","c"],
          [1,2,3],
          ["x","y","z"]]
    print("%s" % rotateImage(six))
    print(rotateImage2(six))
    print(rotateImage3(six))


