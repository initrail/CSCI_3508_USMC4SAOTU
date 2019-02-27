import random, sys
import numpy as np

width = 7
height = 6
gridRow = np.zeros(shape=(height, width), dtype=int)
gridCol = np.zeros(shape=(width, height), dtype=int)


# need grid
def validMoveRow(grid, col):
    '''
    Validates that a column has an available space on the game board by checking
        top row for empty (row-major format)
    :param col: column number
    :return: True if column top row is empty, otherwise False
    '''
    if grid[0][col] == 0:
        grid[0][col] = 1
        return True
    return False


def validMoveCol(grid, col):
    '''
    Validates that a column has an available space on the game board by checking
        top row for empty (column-major format)
    :param col: column number
    :return: True if column top row is empty, otherwise False
    '''
    if grid[col][0] == 0:
        grid[col][0] = 1
        return True
    return False


def randMove(grid):
    '''
    Generates a random column number in which to drop a game piece
    :param grid: game board
    :return: valid column number for move
    '''
    valid = False
    while not valid:
        col = int(random.random()*100) % width
        if validMoveCol(grid, col):
            valid = True

    return col



'''
for i in range(len(gridRow[0])-1):
    gridRow[0][i] = 1
gridRow[0][2] = 0
print(randMove(gridRow))
print(gridRow)
'''

for i in range(width - 1):
    gridCol[i][0] = 1
gridCol[2][0] = 0
sys.stderr.write(str(randMove(gridCol)) + '\n')
sys.stderr.write(str(gridCol))
